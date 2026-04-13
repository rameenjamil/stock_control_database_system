def view_categories(cursor):
    cursor.execute("SELECT category_id, category_name FROM category")
    rows = cursor.fetchall()

    print("\nCategories:")
    for row in rows:
        print(f"{row[0]}: {row[1]}")


def view_suppliers(cursor):
    cursor.execute("SELECT supplier_id, supplier_name FROM supplier")
    rows = cursor.fetchall()

    print("\nSuppliers:")
    for row in rows:
        print(f"{row[0]}: {row[1]}")
