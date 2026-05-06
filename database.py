"""
Database management module for the Stock Control Database application.

This module is responsible for establishing the SQLite database
connection and creating the required database tables if they do
not already exist.

Responsibilities:
- Connect to the SQLite database
- Enable database configuration settings
- Create application tables
- Maintain database schema consistency
"""

import sqlite3 as db


def connect_db():
    """
Establishes a connection to the SQLite database.

This function creates and returns both the database connection and
cursor objects required for executing SQL statements. Foreign key
support is also enabled for relational integrity.

Returns:
    tuple:
        A tuple containing:
        - connection: SQLite database connection object
        - cursor: SQLite cursor object
"""
    connection = db.connect("stock.db")
    cursor = connection.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support

    return connection, cursor


def create_tables(connection, cursor):
    """
Creates all required database tables if they do not already exist.

This function initializes the database schema for categories,
clothing types, suppliers, and products. Foreign key relationships
are also configured to maintain data integrity.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
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
