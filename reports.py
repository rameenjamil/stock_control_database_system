"""
Reports and analytics module for the Stock Control Database application.

This module is responsible for generating inventory reports,
summary statistics, and analytical views of the database records.
It provides insights into stock levels, product distribution,
and supplier-related information.

Responsibilities:
- Generate stock reports
- Display inventory summaries
- Analyze database information
- Provide formatted reporting output
- Support business decision-making
"""

from utility import print_table, get_choice, warning, error, success


def report_total_value(cursor):
    """
Calculates and displays the total value of all stock inventory.

This function retrieves the total inventory value by multiplying
product quantities by their corresponding prices and summing the
results. The calculated stock value is then displayed to the user.

Args:
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    cursor.execute("SELECT SUM(quantity * price) FROM product")
    result = cursor.fetchone()

    total = result[0] if result[0] else 0

    warning("\nTotal Stock Value:")
    print(f"£{total:.2f}")


def report_products_per_category(cursor):
    """
Generates a report showing the number of products in each category.

This function retrieves category names and counts the products
assigned to each category using SQL aggregation. The results
are displayed in a formatted table for easy analysis.

Args:
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    cursor.execute("""
        SELECT category.category_name, COUNT(*)
        FROM product
        JOIN category ON product.category_id = category.category_id
        GROUP BY category.category_name
    """)

    rows = cursor.fetchall()

    if not rows:
        error("\nNo data available.")
        return

    headers = ["Category", "Number of Products"]
    widths = [25, 20]

    warning("\nProducts per Category:")
    print_table(headers, rows, widths)


def report_low_stock(cursor):
    """
Displays products with low stock quantities.

This function retrieves all products whose quantity is below
the low-stock threshold value and presents them in a formatted
table to assist with inventory monitoring and restocking.

Args:
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    cursor.execute("""
        SELECT name, quantity
        FROM product
        WHERE quantity < 10
    """)

    rows = cursor.fetchall()

    if not rows:
        warning("\nNo low stock items.")
        return

    headers = ["Product", "Quantity"]
    widths = [25, 10]

    warning("\nLow Stock Items:")
    print_table(headers, rows, widths)


def show_reports_menu(cursor):
    """
Displays and manages the reports menu interface.

This function presents the available reporting options to the user,
processes menu selections, and calls the corresponding report
generation functions until the user chooses to return to the
previous menu.

Args:
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    choice = ""

    while choice != "0":
        choice = get_choice("Reports Menu:", [
            "1. Total Stock Value",
            "2. Products per Category",
            "3. Low Stock Items",
            "0. Back"
        ])

        if choice == "1":
            report_total_value(cursor)

        elif choice == "2":
            report_products_per_category(cursor)

        elif choice == "3":
            report_low_stock(cursor)
