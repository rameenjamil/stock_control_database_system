from utility import print_table


def view_categories(cursor):
    cursor.execute("SELECT category_id, category_name FROM category")
    rows = cursor.fetchall()

    if not rows:
        print("\nNo categories found.")
        return

    print("\nCategories:")

    headers = ["ID", "Name"]
    widths = [5, 20]

    print_table(headers, rows, widths)


def view_suppliers(cursor):
    cursor.execute(
        "SELECT supplier_id, supplier_name, contact_info FROM supplier")
    rows = cursor.fetchall()

    if not rows:
        print("\nNo suppliers found.")
        return

    print("\nSuppliers:")
    headers = ["ID", "Name", "Contact Info"]
    widths = [5, 20, 30]
    print_table(headers, rows, widths)


def view_products(cursor):
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
        print("\nNo products found.")
        return

    print("\nProducts:")
    headers = ["ID", "Name", "Size", "Quantity",
               "Price", "Category", "Supplier", "Type"]
    widths = [5, 20, 10, 10, 10, 20, 20, 20]
    print_table(headers, rows, widths)


def view_clothing_types(cursor):
    cursor.execute("SELECT type_id, type_name FROM clothing_type")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo clothing type found.")
        return

    print("\nClothing Types:")
    headers = ["ID", "Name"]
    widths = [5, 20]
    print_table(headers, rows, widths)
