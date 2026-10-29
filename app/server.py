"""
Online Food Ordering System - Application Server
SESD Assignment 5 - Agile/Scrum Simulation
Student: M. Hemavardhan (2403A51422) | SR University
"""

import http.server
import socketserver
import json
import sqlite3
import os
import re
import uuid
import hashlib
from urllib.parse import urlparse, parse_qs

PORT = int(os.environ.get("PORT", 8080))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
DB_PATH = os.path.join(BASE_DIR, "food_ordering.db")

# In-memory session store: token -> user_dict
SESSIONS = {}

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def hash_pw(password):
    salt = "sesd_secure_salt"
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

class FoodOrderingHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def read_json_body(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                return json.loads(body)
            except Exception:
                return None
        return None

    def get_auth_user(self):
        auth_header = self.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ', 1)[1]
            return SESSIONS.get(token)
        return None

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # API Routes
        if path == "/api/restaurants":
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM restaurants")
            rows = [dict(r) for r in cursor.fetchall()]
            conn.close()
            return self.send_json({"success": True, "restaurants": rows})

        elif match := re.match(r"^/api/restaurants/(\d+)/menu$", path):
            restaurant_id = int(match.group(1))
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM restaurants WHERE id = ?", (restaurant_id,))
            restaurant = cursor.fetchone()
            if not restaurant:
                conn.close()
                return self.send_json({"error": "Restaurant not found"}, 404)
            
            cursor.execute("SELECT * FROM menu_items WHERE restaurant_id = ?", (restaurant_id,))
            items = [dict(r) for r in cursor.fetchall()]
            conn.close()
            return self.send_json({
                "success": True,
                "restaurant": dict(restaurant),
                "menu": items
            })

        elif path == "/api/me":
            user = self.get_auth_user()
            if not user:
                return self.send_json({"error": "Unauthorized"}, 401)
            return self.send_json({"success": True, "user": user})

        elif path == "/api/orders":
            user = self.get_auth_user()
            if not user:
                return self.send_json({"error": "Unauthorized"}, 401)
            
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT o.*, r.name as restaurant_name 
                FROM orders o
                JOIN restaurants r ON o.restaurant_id = r.id
                WHERE o.user_id = ?
                ORDER BY o.id DESC
            """, (user["id"],))
            orders = [dict(r) for r in cursor.fetchall()]
            
            # Fetch order items for each order
            for o in orders:
                cursor.execute("SELECT * FROM order_items WHERE order_id = ?", (o["id"],))
                o["items"] = [dict(it) for it in cursor.fetchall()]

            conn.close()
            return self.send_json({"success": True, "orders": orders})

        elif match := re.match(r"^/api/orders/([^/]+)/track$", path):
            order_num = match.group(1)
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT o.*, r.name as restaurant_name, r.delivery_time_mins, r.image_emoji
                FROM orders o
                JOIN restaurants r ON o.restaurant_id = r.id
                WHERE o.order_number = ?
            """, (order_num,))
            order = cursor.fetchone()
            if not order:
                conn.close()
                return self.send_json({"error": "Order not found"}, 404)
            
            order_dict = dict(order)
            cursor.execute("SELECT * FROM order_items WHERE order_id = ?", (order_dict["id"],))
            order_dict["items"] = [dict(it) for it in cursor.fetchall()]
            conn.close()

            # Define progression states
            stages = ["Placed", "Confirmed", "Preparing", "Out for Delivery", "Delivered"]
            current_stage_idx = stages.index(order_dict["order_status"]) if order_dict["order_status"] in stages else 0

            return self.send_json({
                "success": True,
                "order": order_dict,
                "stages": stages,
                "current_stage_index": current_stage_idx
            })

        # Static Assets Fallback
        if path == "/" or path == "":
            path = "/index.html"
        
        file_path = os.path.join(PUBLIC_DIR, path.lstrip("/"))
        if os.path.exists(file_path) and os.path.isfile(file_path):
            self.send_response(200)
            if file_path.endswith(".html"):
                self.send_header("Content-Type", "text/html; charset=utf-8")
            elif file_path.endswith(".css"):
                self.send_header("Content-Type", "text/css; charset=utf-8")
            elif file_path.endswith(".js"):
                self.send_header("Content-Type", "application/javascript; charset=utf-8")
            elif file_path.endswith(".json"):
                self.send_header("Content-Type", "application/json")
            self.end_headers()
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
            return
        
        self.send_json({"error": "Not Found"}, 404)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        body = self.read_json_body() or {}

        if path == "/api/register":
            name = body.get("name", "").strip()
            email = body.get("email", "").strip().lower()
            password = body.get("password", "")
            phone = body.get("phone", "").strip()
            address = body.get("address", "").strip()

            if not name or not email or not password:
                return self.send_json({"error": "Name, email, and password are required"}, 400)
            if len(password) < 6:
                return self.send_json({"error": "Password must be at least 6 characters long"}, 400)
            if "@" not in email:
                return self.send_json({"error": "Valid email address is required"}, 400)

            conn = get_db()
            cursor = conn.cursor()
            try:
                pw_hash = hash_pw(password)
                cursor.execute("""
                    INSERT INTO users (name, email, password_hash, phone, address)
                    VALUES (?, ?, ?, ?, ?)
                """, (name, email, pw_hash, phone, address))
                conn.commit()
                user_id = cursor.lastrowid
                conn.close()

                token = str(uuid.uuid4())
                user_data = {"id": user_id, "name": name, "email": email, "phone": phone, "address": address}
                SESSIONS[token] = user_data

                return self.send_json({
                    "success": True,
                    "message": "User registered successfully",
                    "token": token,
                    "user": user_data
                }, 201)
            except sqlite3.IntegrityError:
                conn.close()
                return self.send_json({"error": "User with this email already exists"}, 409)

        elif path == "/api/login":
            email = body.get("email", "").strip().lower()
            password = body.get("password", "")

            if not email or not password:
                return self.send_json({"error": "Email and password are required"}, 400)

            conn = get_db()
            cursor = conn.cursor()
            pw_hash = hash_pw(password)
            cursor.execute("SELECT * FROM users WHERE email = ? AND password_hash = ?", (email, pw_hash))
            user = cursor.fetchone()
            conn.close()

            if not user:
                return self.send_json({"error": "Invalid email or password"}, 401)

            token = str(uuid.uuid4())
            user_data = {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "phone": user["phone"],
                "address": user["address"]
            }
            SESSIONS[token] = user_data

            return self.send_json({
                "success": True,
                "message": "Login successful",
                "token": token,
                "user": user_data
            })

        elif path == "/api/checkout":
            user = self.get_auth_user()
            if not user:
                return self.send_json({"error": "Please log in to complete checkout"}, 401)

            restaurant_id = body.get("restaurant_id")
            items = body.get("items", [])
            payment_method = body.get("payment_method", "UPI")
            delivery_address = body.get("delivery_address") or user.get("address") or "Campus Hostel Block A"

            if not restaurant_id or not items:
                return self.send_json({"error": "Cart cannot be empty"}, 400)

            conn = get_db()
            cursor = conn.cursor()

            # Calculate total and verify prices from DB
            subtotal = 0.0
            order_items_to_insert = []
            for item in items:
                cursor.execute("SELECT * FROM menu_items WHERE id = ? AND restaurant_id = ?", (item["id"], restaurant_id))
                menu_item = cursor.fetchone()
                if not menu_item:
                    conn.close()
                    return self.send_json({"error": f"Invalid item: {item.get('name')}"}, 400)
                
                qty = max(1, int(item.get("quantity", 1)))
                item_price = float(menu_item["price"])
                subtotal += item_price * qty
                order_items_to_insert.append((menu_item["id"], menu_item["name"], item_price, qty))

            cursor.execute("SELECT delivery_fee FROM restaurants WHERE id = ?", (restaurant_id,))
            rest = cursor.fetchone()
            delivery_fee = float(rest["delivery_fee"]) if rest else 30.0
            total_amount = round(subtotal + delivery_fee, 2)

            # Generate Mock Payment Transaction ID
            txn_id = f"TXN-MOCK-{uuid.uuid4().hex[:10].upper()}"
            order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"

            cursor.execute("""
                INSERT INTO orders (order_number, user_id, restaurant_id, total_amount, payment_method, payment_status, transaction_id, order_status, delivery_address)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'Placed', ?)
            """, (order_number, user["id"], restaurant_id, total_amount, payment_method, "Success (Mock Paid)", txn_id, delivery_address))

            order_id = cursor.lastrowid

            for item_id, item_name, price, qty in order_items_to_insert:
                cursor.execute("""
                    INSERT INTO order_items (order_id, menu_item_id, item_name, price, quantity)
                    VALUES (?, ?, ?, ?, ?)
                """, (order_id, item_id, item_name, price, qty))

            conn.commit()
            conn.close()

            return self.send_json({
                "success": True,
                "message": "Order placed successfully with mock payment verification",
                "order_number": order_number,
                "order_id": order_id,
                "transaction_id": txn_id,
                "total_amount": total_amount,
                "status": "Placed"
            }, 201)

        elif match := re.match(r"^/api/orders/([^/]+)/advance$", path):
            order_num = match.group(1)
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("SELECT id, order_status FROM orders WHERE order_number = ?", (order_num,))
            order = cursor.fetchone()
            if not order:
                conn.close()
                return self.send_json({"error": "Order not found"}, 404)

            stages = ["Placed", "Confirmed", "Preparing", "Out for Delivery", "Delivered"]
            curr = order["order_status"]
            idx = stages.index(curr) if curr in stages else 0
            next_idx = min(idx + 1, len(stages) - 1)
            new_status = stages[next_idx]

            cursor.execute("UPDATE orders SET order_status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (new_status, order["id"]))
            conn.commit()
            conn.close()

            return self.send_json({
                "success": True,
                "previous_status": curr,
                "new_status": new_status,
                "is_completed": (new_status == "Delivered")
            })

        self.send_json({"error": "Endpoint not found"}, 404)

def run():
    # Automatically initialize DB if missing
    if not os.path.exists(DB_PATH):
        import init_db
        init_db.initialize_database()

    with socketserver.TCPServer(("", PORT), FoodOrderingHandler) as httpd:
        print(f"🚀 Food Ordering Server running at http://localhost:{PORT}")
        print(f"Student: M. Hemavardhan (2403A51422) - SESD Assignment 5")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")

if __name__ == "__main__":
    run()
