import sqlite3 as db


def connect_db():
    connection = db.connect("stock.db")
    cursor = connection.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support

    return connection, cursor


def create_tables(connection, cursor):

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clothing_type (
            type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS supplier (
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_name TEXT NOT NULL,
            contact_info TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            size TEXT,
            quantity INTEGER,
            price REAL,
            category_id INTEGER,
            supplier_id INTEGER,
            type_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE RESTRICT,
            FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id) ON DELETE RESTRICT,
            FOREIGN KEY (type_id) REFERENCES clothing_type(type_id) ON DELETE RESTRICT
        )
    ''')

    connection.commit()
