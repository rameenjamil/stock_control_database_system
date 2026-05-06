"""
View module for displaying database records.

This module contains functions responsible for retrieving and
presenting formatted database information to the user. It separates
data visualization from business logic and CRUD operations.

Responsibilities:
- Display categories
- Display suppliers
- Display products
- Display clothing types
- Format output consistently
"""

from utility import print_table, warning, error


def view_categories(cursor):
    """
Displays all category records in a formatted table.

This function retrieves category information from the database
and presents it in a structured and readable format.

Args:
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    cursor.execute("SELECT category_id, category_name FROM category")
    rows = cursor.fetchall()

    if not rows:
        error("\nNo categories found.")
        return

    warning("\nCategories:")

    headers = ["ID", "Name"]
    widths = [5, 20]

    print_table(headers, rows, widths)


def view_suppliers(cursor):
    """
Displays all supplier records in a formatted table.

This function retrieves supplier names and contact information
from the database and displays them in an organized layout.

Args:
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    cursor.execute(
        "SELECT supplier_id, supplier_name, contact_info FROM supplier")
    rows = cursor.fetchall()

    if not rows:
        error("\nNo suppliers found.")
        return

    warning("\nSuppliers:")
    headers = ["ID", "Name", "Contact Info"]
    widths = [5, 20, 30]
    print_table(headers, rows, widths)


def view_products(cursor):
    """
Displays all product records with related database information.

This function retrieves products along with their associated
category, supplier, and clothing type using SQL joins. The
results are displayed in a formatted table for easy reading.

Args:
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    cursor.execute("""
                   SELECT
                   product.product_id,
                   product.name,
                   product.size,
                   product.quantity,
                   product.price,
                   category.category_name,
                   supplier.supplier_name,
                   clothing_type.type_name
                   FROM product
                   JOIN category ON product.category_id = category.category_id
                   JOIN supplier ON product.supplier_id = supplier.supplier_id
                   JOIN clothing_type ON product.type_id = clothing_type.type_id
                   """)

    rows = cursor.fetchall()
    if not rows:
        error("\nNo products found.")
        return

    warning("\nProducts:")
    headers = ["ID", "Name", "Size", "Quantity",
               "Price", "Category", "Supplier", "Type"]
    widths = [5, 20, 10, 10, 10, 20, 20, 20]
    print_table(headers, rows, widths)


def view_clothing_types(cursor):
    """
Displays all clothing type records.

This function retrieves clothing type data from the database
and prints it in a simple tabular format.

Args:
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    cursor.execute("SELECT type_id, type_name FROM clothing_type")
    rows = cursor.fetchall()
    if not rows:
        error("\nNo clothing type found.")
        return

    warning("\nClothing Types:")
    headers = ["ID", "Name"]
    widths = [5, 20]
    print_table(headers, rows, widths)
