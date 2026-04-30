from utility import print_table, get_choice, warning, error, success


def report_total_value(cursor):
    cursor.execute("SELECT SUM(quantity * price) FROM product")
    result = cursor.fetchone()

    total = result[0] if result[0] else 0

    warning("\nTotal Stock Value:")
    print(f"£{total:.2f}")


def report_products_per_category(cursor):
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
