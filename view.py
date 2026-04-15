def view_categories(cursor):
    cursor.execute("SELECT category_id, category_name FROM category")
    rows = cursor.fetchall()

    print("\nCategories:")
    print(f"ID    Name")
    print("-" * 15)
    for row in rows:
        print(f"{row[0]:<5}{row[1]}")


def view_suppliers(cursor):
    cursor.execute("SELECT supplier_id, supplier_name FROM supplier")
    rows = cursor.fetchall()

    print("\nSuppliers:")
    print(f"ID    Name")
    print("-" * 15)

    for row in rows:
        print(f"{row[0]:<5}{row[1]}")


def view_products(cursor):
    cursor.execute("""
                   SELECT
                   product.product_id,
                   product.name,
                   product.size,
                   product.quantity,
                   product.price,
                   category.category_name,
                   supplier.supplier_name
                   FROM product
                   JOIN category ON product.category_id = category.category_id
                   JOIN supplier ON product.supplier_id = supplier.supplier_id
                   """)

    results = cursor.fetchall()
    if not results:
        print("\nNo products found.")
        return

    titles = [description[0] for description in cursor.description]
    # set initial column width based on data
    lengths = [len(title) for title in titles]

    for row in results:
        for i in range(len(row)):
            value_length = len(str(row[i]))
            if value_length > lengths[i]:
                lengths[i] = value_length

    # add padding
    lengths = [length + 3 for length in lengths]

    for i in range(len(titles)):
        print(f"{titles[i]:<{lengths[i]}}", end="")
    print()
    # separator
    print("-" * sum(lengths))

    # print rows
    for row in results:
        for i in range(len(row)):
            print(f"{str(row[i]):<{lengths[i]}}", end="")
        print()


def view_clothing_types(cursor):
    cursor.execute("SELECT type_id, type_name FROM clothing_type")
    rows = cursor.fetchall()

    print("\nClothing Types:")
    print(f"ID    Name")
    print("-" * 15)

    for row in rows:
        print(f"{row[0]:<5}{row[1]}")
