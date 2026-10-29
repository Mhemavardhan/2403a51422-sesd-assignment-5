"""
Database initialization and seed script for Online Food Ordering System.
Student: M. Hemavardhan (2403A51422)
Subject: SESD (24CS301PC311) - SR University
"""

import sqlite3
import hashlib
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "food_ordering.db")

def hash_password(password, salt="sesd_secure_salt"):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def initialize_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            phone TEXT,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Restaurants Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cuisine TEXT NOT NULL,
            rating REAL DEFAULT 4.5,
            delivery_time_mins INTEGER DEFAULT 30,
            delivery_fee REAL DEFAULT 40.0,
            image_emoji TEXT DEFAULT '🍽️',
            address TEXT
        )
    """)

    # Menu Items Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category TEXT,
            is_veg INTEGER DEFAULT 1,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
        )
    """)

    # Orders Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_number TEXT UNIQUE NOT NULL,
            user_id INTEGER NOT NULL,
            restaurant_id INTEGER NOT NULL,
            total_amount REAL NOT NULL,
            payment_method TEXT NOT NULL,
            payment_status TEXT NOT NULL,
            transaction_id TEXT,
            order_status TEXT DEFAULT 'Placed',
            delivery_address TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
        )
    """)

    # Order Items Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            menu_item_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (id)
        )
    """)

    # Seed Default User
    demo_pw_hash = hash_password("demo123")
    cursor.execute("""
        INSERT INTO users (name, email, password_hash, phone, address)
        VALUES (?, ?, ?, ?, ?)
    """, ("Hemavardhan", "hemavardhan@sru.edu.in", demo_pw_hash, "+91 9876543210", "SR University Campus, Warangal"))

    # Seed Restaurants
    restaurants_data = [
        ("Paradise Biryani", "Hyderabadi, Biryani & Mughlai", 4.7, 30, 40.0, "🍗", "Hanamkonda Main Road, Warangal"),
        ("Spice Garden Dhaba", "North Indian, Tandoor & Curries", 4.4, 25, 30.0, "🍲", "Subedari Circle, Warangal"),
        ("Bella Trattoria", "Authentic Italian, Pizza & Pasta", 4.8, 35, 50.0, "🍕", "University Road, Warangal"),
        ("Green Leaf Healthy Eats", "Salads, Bowls & Vegan", 4.6, 20, 25.0, "🥗", "Nakkalagutta, Warangal")
    ]

    cursor.executemany("""
        INSERT INTO restaurants (name, cuisine, rating, delivery_time_mins, delivery_fee, image_emoji, address)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, restaurants_data)

    # Seed Menu Items
    menu_data = [
        # Paradise Biryani
        (1, "Hyderabadi Chicken Dum Biryani", "Fragrant basmati rice cooked with tender marinated chicken and rich spices", 280.0, "Main Course", 0),
        (1, "Hyderabadi Paneer Biryani", "Slow cooked basmati rice with marinated paneer cubes and saffron aroma", 240.0, "Main Course", 1),
        (1, "Chicken 65", "Spicy, deep-fried chicken tossed in curry leaves and south Indian spices", 210.0, "Starters", 0),
        (1, "Mirchi Ka Salan", "Traditional peanut and sesame seed curry accompaniment", 60.0, "Sides", 1),
        
        # Spice Garden Dhaba
        (2, "Butter Chicken Boneless", "Tandoor roasted chicken in creamy tomato butter gravy", 270.0, "Main Course", 0),
        (2, "Paneer Butter Masala", "Cottage cheese cubes simmered in rich cashew and tomato sauce", 230.0, "Main Course", 1),
        (2, "Garlic Butter Naan", "Clay oven roasted flatbread topped with garlic and butter", 45.0, "Breads", 1),
        (2, "Dal Makhani", "Slow simmered black lentils finished with cream and white butter", 190.0, "Main Course", 1),

        # Bella Trattoria
        (3, "Margherita Wood-fired Pizza", "San Marzano tomatoes, fresh mozzarella, fresh basil, and extra virgin olive oil", 320.0, "Pizza", 1),
        (3, "Pepperoni & Spicy Sausage Pizza", "Smoked pepperoni, spicy Italian sausage, and mozzarella", 390.0, "Pizza", 0),
        (3, "Penne Alfredo Pasta", "Penne tossed in velvety parmesan cream sauce with herbs", 280.0, "Pasta", 1),
        (3, "Classic Tiramisu", "Espresso soaked ladyfingers layered with whipped mascarpone cream", 190.0, "Dessert", 1),

        # Green Leaf Healthy Eats
        (4, "Mediterranean Quinoa Bowl", "Quinoa, cherry tomatoes, kalamata olives, cucumber, feta cheese, and lemon herb dressing", 260.0, "Bowls", 1),
        (4, "Avocado Caesar Salad", "Crispy romaine, creamy avocado, garlic croutons, and vegan Caesar dressing", 240.0, "Salads", 1),
        (4, "Cold Pressed Orange Carrot Juice", "100% pure fresh fruit and vegetable juice with ginger zest", 120.0, "Beverages", 1),
        (4, "Chia Seed Mango Pudding", "Almond milk chia pudding topped with fresh Alphonso mango purée", 160.0, "Dessert", 1)
    ]

    cursor.executemany("""
        INSERT INTO menu_items (restaurant_id, name, description, price, category, is_veg)
        VALUES (?, ?, ?, ?, ?, ?)
    """, menu_data)

    conn.commit()
    conn.close()
    print("Database initialized successfully with sample restaurants and menus.")

if __name__ == "__main__":
    initialize_database()
