from multiprocessing import connection

from view import view_categories, view_suppliers, view_products, view_clothing_types


def add_product(connection, cursor):

    view_categories(cursor)
    view_suppliers(cursor)
    view_clothing_types(cursor)

    name = input("Enter product name: ")
    size = input("Enter product size: ")
    try:
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))
        category_id = int(input("Enter category ID: "))
        supplier_id = int(input("Enter supplier ID: "))
        type_id = int(input("Enter clothing type ID: "))
    except ValueError:
        print("Invalid input. Please enter the correct datatype.")
        return

# foreign key validation
    cursor.execute(
        "SELECT * FROM category WHERE category_id = ?", (category_id,))
    if not cursor.fetchone():
        print("Invalid category ID.")
        return

    cursor.execute(
        "SELECT * FROM supplier WHERE supplier_id = ?", (supplier_id,))
    if not cursor.fetchone():
        print("Invalid supplier ID.")
        return

    cursor.execute("SELECT * FROM clothing_type WHERE type_id = ?", (type_id,))
    if not cursor.fetchone():
        print("Invalid clothing type ID.")
        return

    cursor.execute("""
                   INSERT INTO product (name, size, quantity, price, category_id, supplier_id, type_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, size, quantity, price, category_id, supplier_id, type_id))

    connection.commit()
    print(f"\nProduct added successfully.")


def add_category(connection, cursor):
    category_name = input("Enter category name: ")
    if not category_name.strip():
        print("Category name cannot be empty.")
        return

    cursor.execute("""
                   INSERT INTO category (category_name)
        VALUES (?)
    """, (category_name,))  # comma is needed because it is a tuple

    connection.commit()
    print(f"\nCategory added successfully.")


def add_supplier(connection, cursor):
    supplier_name = input("Enter supplier name: ")
    contact_info = input("Enter contact info: ")
    if not supplier_name.strip():
        print("Supplier name cannot be empty.")
        return

    cursor.execute("""
                   INSERT INTO supplier (supplier_name, contact_info)
        VALUES (?, ?)
    """, (supplier_name, contact_info))

    connection.commit()
    print("Supplier added successfully.")


def add_clothing_type(connection, cursor):
    type_name = input("Enter clothing type name: ")
    if not type_name.strip():
        print("Clothing type name cannot be empty.")
        return

    cursor.execute("""
                   INSERT INTO clothing_type (type_name)
        VALUES (?)
    """, (type_name,))

    connection.commit()
    print("Clothing type added successfully.")


def update_product(connection, cursor):
    view_products(cursor)

    try:
        product_id = int(input("Enter the ID of the product to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    cursor.execute("SELECT * FROM product WHERE product_id = ?", (product_id,))
    if not cursor.fetchone():
        print("Product not found.")
        return

    print("""\nWhat would you like to update?
          1. Name
          2. Size
          3. Quantity
          4. Price""")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice == 1:
        new_value = input("Enter the new name: ")
        query = "UPDATE product SET name = ? WHERE product_id = ?", (
            new_value, product_id)
    elif choice == 2:
        new_value = input("Enter the new size: ")
        query = "UPDATE product SET size = ? WHERE product_id = ?", (
            new_value, product_id)
    elif choice == 3:
        try:
            new_value = input("Enter the new quantity: ")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        query = "UPDATE product SET quantity = ? WHERE product_id = ?", (
            new_value, product_id)
    elif choice == 4:
        try:
            new_value = input("Enter the new price: ")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        query = "UPDATE product SET price = ? WHERE product_id = ?", (
            new_value, product_id)

    else:
        print("Invalid choice.")
        return

    cursor.execute(query, (new_value, product_id,))
    connection.commit()
    print("Product updated successfully.")

    print("Selected ID : ", product_id)

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


def delete_category(connection, cursor):
    view_categories(cursor)

    try:
        category_id = int(input("Enter the ID of the category to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    cursor.execute(
        "SELECT * FROM category WHERE category_id = ?", (category_id,))
    if not cursor.fetchone():
        print("Category not found.")
        return

    cursor.execute(
        "SELECT * FROM product WHERE category_id = ?", (category_id,))
    if cursor.fetchone():
        print("Cannot delete category. There are products associated with this category.")
        return

    confirm = input(
        "Are you sure you want to delete this category? (y/n): ").lower()

    if confirm == "y":
        cursor.execute(
            "DELETE FROM category WHERE category_id = ?", (category_id,))
        connection.commit()
        print("Category deleted successfully.")

    else:
        print("Deletion cancelled.")


def delete_supplier(connection, cursor):
    view_suppliers(cursor)

    try:
        supplier_id = int(input("Enter the ID of the supplier to delete: "))
    except ValueError:
        print("Invalid input.")
        return

    cursor.execute(
        "SELECT * FROM supplier WHERE supplier_id = ?", (supplier_id,))
    if not cursor.fetchone():
        print("Supplier not found.")
        return

    # prevent breaking product table
    cursor.execute(
        "SELECT * FROM product WHERE supplier_id = ?", (supplier_id,))
    if cursor.fetchone():
        print("Cannot delete supplier. It is used by products.")
        return

    confirm = input("Are you sure? (y/n): ").lower()

    if confirm == "y":
        cursor.execute(
            "DELETE FROM supplier WHERE supplier_id = ?", (supplier_id,))
        connection.commit()
        print("Supplier deleted successfully.")
    else:
        print("Cancelled.")


def delete_clothing_type(connection, cursor):
    view_clothing_types(cursor)

    try:
        type_id = int(input("Enter the ID of the clothing type to delete: "))
    except ValueError:
        print("Invalid input.")
        return

    cursor.execute("SELECT * FROM clothing_type WHERE type_id = ?", (type_id,))
    if not cursor.fetchone():
        print("Clothing type not found.")
        return

    cursor.execute("SELECT * FROM product WHERE type_id = ?", (type_id,))
    if cursor.fetchone():
        print("Cannot delete clothing type. It is used by products.")
        return

    confirm = input("Are you sure? (y/n): ").lower()

    if confirm == "y":
        cursor.execute(
            "DELETE FROM clothing_type WHERE type_id = ?", (type_id,))
        connection.commit()
        print("Clothing type deleted successfully.")
    else:
        print("Cancelled.")
