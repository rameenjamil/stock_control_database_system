from view import view_categories, view_suppliers, view_products, view_clothing_types


def add_product(connection, cursor):

    view_categories(cursor)
    view_suppliers(cursor)
    view_clothing_types(cursor)

    name = input("Enter product name: ")
    size = input("Enter product size: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    category_id = int(input("Enter category ID: "))
    supplier_id = int(input("Enter supplier ID: "))
    type_id = int(input("Enter clothing type ID: "))

    cursor.execute("""
                   INSERT INTO product (name, size, quantity, price, category_id, supplier_id, type_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, size, quantity, price, category_id, supplier_id, type_id))

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


def update_product(connection, cursor):
    view_products(cursor)

    product_id = int(input("Enter the ID of the product to update: "))

    print("""\nWhat would you like to update?
          1. Name
          2. Size
          3. Quantity
          4. Price""")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        new_value = input("Enter the new name: ")
        cursor.execute(
            "UPDATE product SET name = ? WHERE product_id = ?", (new_value, product_id))
    elif choice == 2:
        new_value = input("Enter the new size: ")
        cursor.execute(
            "UPDATE product SET size = ? WHERE product_id = ?", (new_value, product_id))
    elif choice == 3:
        new_value = input("Enter the new quantity: ")
        cursor.execute(
            "UPDATE product SET quantity = ? WHERE product_id = ?", (new_value, product_id))
    elif choice == 4:
        new_value = input("Enter the new price: ")
        cursor.execute(
            "UPDATE product SET price = ? WHERE product_id = ?", (new_value, product_id))

    else:
        print("Invalid choice.")
        return

    connection.commit()
    print("Product updated successfully.")

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
    WHERE product.product_id = ?
""", (product_id,))

    print("slected ID : ", product_id)

    updated = cursor.fetchone()

    if updated:
        print(f"""
              ID: {updated[0]}
              Name: {updated[1]}
              Size: {updated[2]}
              Quantity: {updated[3]}
              Price: {updated[4]}
              Category: {updated[5]}
              Supplier: {updated[6]}
              Type: {updated[7]}""")
    else:
        print("\nError fetching updated record.")


def delete_product(connection, cursor):
    view_products(cursor)

    try:
        product_id = int(input("Enter the ID of the product to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    cursor.execute("SELECT * FROM product WHERE product_id = ?", (product_id,))
    record = cursor.fetchone()

    if not record:
        print("Product not found.")
        return

    confirm = input(
        "Are you sure you want to delete this product? (y/n): ").lower()

    if confirm == "y":
        cursor.execute(
            "DELETE FROM product WHERE product_id = ?", (product_id,))
        connection.commit()
        print("Product deleted successfully.")
    else:
        print("Deletion cancelled.")
