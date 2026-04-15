from view import view_categories, view_suppliers


def add_product(connection, cursor):

    view_categories(cursor)
    view_suppliers(cursor)

    name = input("Enter product name: ")
    size = input("Enter product size: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    category_id = int(input("Enter category ID: "))
    supplier_id = int(input("Enter supplier ID: "))

    cursor.execute("""
                   INSERT INTO product (name, size, quantity, price, category_id, supplier_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, size, quantity, price, category_id, supplier_id))

    connection.commit()
    print("Product added successfully.")


def add_category(connection, cursor):
    category_name = input("Enter category name: ")

    cursor.execute("""
                   INSERT INTO category (category_name)
        VALUES (?)
    """, (category_name,))  # comma is needed because it is a tuple

    connection.commit()
    print("Category added successfully.")


def add_supplier(connection, cursor):
    supplier_name = input("Enter supplier name: ")
    contact_info = input("Enter contact info: ")

    cursor.execute("""
                   INSERT INTO supplier (supplier_name, contact_info)
        VALUES (?, ?)
    """, (supplier_name, contact_info))

    connection.commit()
    print("Supplier added successfully.")


def add_clothing_type(connection, cursor):
    type_name = input("Enter clothing type name: ")

    cursor.execute("""
                   INSERT INTO clothing_type (type_name)
        VALUES (?)
    """, (type_name,))  # comma is needed because it is a tuple

    connection.commit()
    print("Clothing type added successfully.")
