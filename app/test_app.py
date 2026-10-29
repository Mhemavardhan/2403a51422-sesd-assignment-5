"""
Unit and Integration Test Suite for Online Food Ordering App
SESD Assignment 5: Agile/Scrum Simulation
Student: M. Hemavardhan (2403A51422) - SR University
"""

import unittest
import sqlite3
import os
import sys
import json
import uuid

# Add app directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import init_db
import server

class TestFoodOrderingSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize fresh test database
        cls.db_path = os.path.join(os.path.dirname(__file__), "food_ordering.db")
        init_db.initialize_database()

    def test_01_database_tables_exist(self):
        """Verify all essential schema tables exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()

        for expected in ["users", "restaurants", "menu_items", "orders", "order_items"]:
            self.assertIn(expected, tables, f"Missing expected table: {expected}")

    def test_02_password_hashing_security(self):
        """Verify passwords are salted and hashed securely using SHA-256"""
        raw_pw = "mySecretPassword123"
        hashed = server.hash_pw(raw_pw)
        self.assertNotEqual(raw_pw, hashed)
        self.assertEqual(len(hashed), 64)  # SHA-256 hex string length
        # Deterministic check with same salt
        self.assertEqual(hashed, server.hash_pw(raw_pw))

    def test_03_default_seeded_restaurants(self):
        """Verify restaurants and menu items are properly seeded"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) as count FROM restaurants")
        r_count = cursor.fetchone()["count"]
        self.assertGreaterEqual(r_count, 4)

        cursor.execute("SELECT count(*) as count FROM menu_items")
        m_count = cursor.fetchone()["count"]
        self.assertGreaterEqual(m_count, 12)
        conn.close()

    def test_04_user_registration_and_authentication(self):
        """Test Sprint 1: Customer Login and Registration (User Story #1)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        test_email = f"student_{uuid.uuid4().hex[:6]}@sru.edu.in"
        test_pw = "securePass2026"
        pw_hash = server.hash_pw(test_pw)

        # Register
        cursor.execute("""
            INSERT INTO users (name, email, password_hash, phone, address)
            VALUES (?, ?, ?, ?, ?)
        """, ("M. Hemavardhan", test_email, pw_hash, "+91 9876543210", "Hostel Block A, SRU"))
        conn.commit()
        user_id = cursor.lastrowid
        self.assertIsNotNone(user_id)

        # Authenticate
        cursor.execute("SELECT * FROM users WHERE email = ? AND password_hash = ?", (test_email, pw_hash))
        authenticated_user = cursor.fetchone()
        self.assertIsNotNone(authenticated_user)

        # Duplicate email should fail (IntegrityError)
        with self.assertRaises(sqlite3.IntegrityError):
            cursor.execute("""
                INSERT INTO users (name, email, password_hash, phone, address)
                VALUES (?, ?, ?, ?, ?)
            """, ("Duplicate User", test_email, pw_hash, "+91 0000000000", "Campus"))
            conn.commit()

        conn.close()

    def test_05_cart_and_mock_checkout(self):
        """Test Sprint 2: Shopping Cart and Mock Payment (User Stories #4 & #5)"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Fetch restaurant and 2 menu items
        cursor.execute("SELECT * FROM restaurants LIMIT 1")
        rest = cursor.fetchone()
        restaurant_id = rest["id"]
        delivery_fee = float(rest["delivery_fee"])

        cursor.execute("SELECT * FROM menu_items WHERE restaurant_id = ? LIMIT 2", (restaurant_id,))
        items = cursor.fetchall()
        self.assertGreaterEqual(len(items), 2)

        # Calculate Cart
        item1 = items[0]
        item2 = items[1]
        qty1 = 2
        qty2 = 1
        expected_subtotal = (float(item1["price"]) * qty1) + (float(item2["price"]) * qty2)
        expected_grand_total = round(expected_subtotal + delivery_fee, 2)

        # Place Order
        order_num = f"ORD-TEST-{uuid.uuid4().hex[:6].upper()}"
        mock_txn = f"TXN-MOCK-{uuid.uuid4().hex[:8].upper()}"

        cursor.execute("""
            INSERT INTO orders (order_number, user_id, restaurant_id, total_amount, payment_method, payment_status, transaction_id, order_status, delivery_address)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'Placed', ?)
        """, (order_num, 1, restaurant_id, expected_grand_total, "UPI", "Success (Mock Paid)", mock_txn, "SR University Hostels"))
        order_id = cursor.lastrowid

        cursor.execute("INSERT INTO order_items (order_id, menu_item_id, item_name, price, quantity) VALUES (?, ?, ?, ?, ?)",
                       (order_id, item1["id"], item1["name"], item1["price"], qty1))
        cursor.execute("INSERT INTO order_items (order_id, menu_item_id, item_name, price, quantity) VALUES (?, ?, ?, ?, ?)",
                       (order_id, item2["id"], item2["name"], item2["price"], qty2))
        conn.commit()

        # Verify Order items
        cursor.execute("SELECT sum(price * quantity) as subtotal FROM order_items WHERE order_id = ?", (order_id,))
        db_subtotal = cursor.fetchone()["subtotal"]
        self.assertEqual(round(db_subtotal, 2), round(expected_subtotal, 2))

        conn.close()

    def test_06_order_tracking_progression(self):
        """Test Sprint 3: Order Tracking Lifecycle (User Story #6)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        order_num = f"ORD-TRACK-{uuid.uuid4().hex[:6].upper()}"
        cursor.execute("""
            INSERT INTO orders (order_number, user_id, restaurant_id, total_amount, payment_method, payment_status, transaction_id, order_status, delivery_address)
            VALUES (?, 1, 1, 350.0, 'UPI', 'Success (Mock Paid)', 'TXN-MOCK-TEST', 'Placed', 'SR University Campus')
        """, (order_num,))
        conn.commit()

        stages = ["Placed", "Confirmed", "Preparing", "Out for Delivery", "Delivered"]
        for i in range(1, len(stages)):
            next_stage = stages[i]
            cursor.execute("UPDATE orders SET order_status = ? WHERE order_number = ?", (next_stage, order_num))
            conn.commit()

            cursor.execute("SELECT order_status FROM orders WHERE order_number = ?", (order_num,))
            current_status = cursor.fetchone()[0]
            self.assertEqual(current_status, next_stage)

        conn.close()

if __name__ == "__main__":
    unittest.main()
