from dataclasses import fields

from view import view_categories, view_suppliers, view_products, view_clothing_types


def select_from_table(cursor, table, id_col, name_col):
    """
    Displays all records from a table and allows the user to select one.

    The records are shown as a numbered list using the specified name column.
    The user selects an option by entering a number, and the function returns
    the ID of the selected record.

    If the table is empty or the user enters an invalid choice, the function
    returns None.
    """
    cursor.execute(f"SELECT {id_col}, {name_col} FROM {table}")
    rows = cursor.fetchall()

    if not rows:
        print(
            f"\nNo records found in {table.replace('_', ' ')}. Please add one first.")
        return None
    # replaces underscores with spaces and capitalizes each word
    print(f"\nSelect {table.replace('_', ' ').title()}:")
    for i, row in enumerate(rows, start=1):
        print(f"{i}. {row[1]}")

    try:
        choice = int(input("Choose an option: "))
        return rows[choice - 1][0]  # return the ID of the selected record
    except (ValueError, IndexError):
        print("Invalid choice.")
        return None


def add_product(connection, cursor):
    """
    Adds a new product to the database using user-friendly selection
    for category, supplier, and clothing type.
    """

    name = input("Enter product name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    size = input("Enter product size: ").strip()

    try:
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))
    except ValueError:
        print("Invalid input. Please enter the correct datatype.")
        return

    category_id = select_from_table(
        cursor, "category", "category_id", "category_name")
    if not category_id:
        return

    supplier_id = select_from_table(
        cursor, "supplier", "supplier_id", "supplier_name")
    if not supplier_id:
        return

    type_id = select_from_table(
        cursor, "clothing_type", "type_id", "type_name")
    if not type_id:
        return

    cursor.execute("""
                   INSERT INTO product (name, size, quantity, price, category_id, supplier_id, type_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, size, quantity, price, category_id, supplier_id, type_id))

    connection.commit()
    print(f"\nProduct added successfully.")


def add_category(connection, cursor):
    """
    Adds a new category to the database with input validation.
    """

    category_name = input("Enter category name: ").strip()
    if not category_name:
        print("Category name cannot be empty.")
        return

    # checking for duplicates
    cursor.execute(
        "SELECT * FROM category WHERE category_name = ?", (category_name,))
    if cursor.fetchone():
        print("Category already exists.")
        return

    cursor.execute("INSERT INTO category (category_name) VALUES (?)",
                   (category_name,))  # comma is needed because it is a tuple

    connection.commit()
    print(f"\nCategory added successfully.")


def add_supplier(connection, cursor):
    """
    Adds a new supplier to the database with input validation.
    """

    supplier_name = input("Enter supplier name: ").strip()
    contact_info = input("Enter contact info: ").strip()
    if not supplier_name:
        print("Supplier name cannot be empty.")
        return

    # checking for duplicates
    cursor.execute(
        "SELECT * FROM supplier WHERE supplier_name = ?", (supplier_name,))
    if cursor.fetchone():
        print("Supplier already exists.")
        return

    cursor.execute("INSERT INTO supplier (supplier_name, contact_info)VALUES (?, ?)",
                   (supplier_name, contact_info))

    connection.commit()
    print("\nSupplier added successfully.")


def add_clothing_type(connection, cursor):
    """
    Adds a new clothing type to the database with input validation.
    """
    type_name = input("Enter clothing type name: ").strip()

    if not type_name:
        print("Clothing type name cannot be empty.")
        return

    # checking for duplicates
    cursor.execute(
        "SELECT * FROM clothing_type WHERE type_name = ?", (type_name,))
    if cursor.fetchone():
        print("Clothing type already exists.")
        return

    cursor.execute("""
                   INSERT INTO clothing_type (type_name)
        VALUES (?)
    """, (type_name,))

    connection.commit()
    print("\nClothing type added successfully.")


def update_product(connection, cursor):
    """
    Updates a selected field of a product.
    """
    view_products(cursor)

    try:
        product_id = int(input("Enter product ID to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    cursor.execute("SELECT * FROM product WHERE product_id = ?", (product_id,))
    if not cursor.fetchone():
        print("Product not found.")
        return

    fields = {
        "1": ("Name", "name", str),
        "2": ("Size", "size", str),
        "3": ("Quantity", "quantity", int),
        "4": ("Price", "price", float)
    }

    print("\nWhat would you like to update?")
    for key, value in fields.items():
        print(f"{key}. {value[0]}")

    choice = input("Enter choice: ")
    if choice not in fields:
        print("Invalid choice.")
        return

    label, column, data_type = fields[choice]

    column, data_type = fields[choice]

    try:
        new_value = data_type(input(f"Enter new {label.lower()}: "))
    except ValueError:
        print("Invalid input type.")
        return

    cursor.execute(
        f"UPDATE product SET {column} = ? WHERE product_id = ?",
        (new_value, product_id)
    )

    connection.commit()
    print("Product updated successfully.")

    # fetch updated record to show user
    cursor.execute("SELECT * FROM product WHERE product_id = ?", (product_id,))
    updated = cursor.fetchone()

    if updated:
        print("\nUpdated Product:")
        print(
            f"ID: {updated[0]}, Name: {updated[1]}, Size: {updated[2]}, Quantity: {updated[3]}, Price: {updated[4]}")


def update_category(connection, cursor):
    """
    Updates the name of a category.

    """
    view_categories(cursor)
    try:
        category_id = int(input("Enter category ID to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    cursor.execute(
        "SELECT * FROM category WHERE category_id = ?", (category_id,))
    if not cursor.fetchone():
        print("Category not found.")
        return

    new_name = input("Enter new category name: ").strip()
    if not new_name:
        print("Category name cannot be empty.")
        return

    cursor.execute(
        "SELECT * FROM category WHERE category_name = ?", (new_name,))
    if cursor.fetchone():
        print("Category name already exists.")
        return

    cursor.execute("UPDATE category SET category_name = ? WHERE category_id = ?",
                   (new_name, category_id))
    connection.commit()
    print("Category updated successfully.")
    view_categories(cursor)


def update_supplier(connection, cursor):
    """
    Updates the name and contact info of a supplier.
    """
    view_suppliers(cursor)

    try:
        supplier_id = int(input("Enter supplier ID to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    cursor.execute(
        "SELECT * FROM supplier WHERE supplier_id = ?", (supplier_id,))
    if not cursor.fetchone():
        print("Supplier not found.")
        return

    print("""
        What would you like to update?
        1. Name
        2. Contact Info
        """)
    choice = input("Enter choice: ")

    if choice == "1":
        new_value = input("Enter new supplier name: ").strip()
        if not new_value:
            print("Supplier name cannot be empty.")
            return
        cursor.execute(
            "SELECT 1 FROM supplier WHERE supplier_name = ?", (new_value,))
        if cursor.fetchone():
            print("Supplier already exists.")
            return
        column = "supplier_name"

    elif choice == "2":
        new_value = input("Enter new contact info: ").strip()
        column = "contact_info"

    else:
        print("Invalid choice.")
        return

    cursor.execute(f"UPDATE supplier SET {column} = ? WHERE supplier_id = ?",
                   (new_value, supplier_id))
    connection.commit()
    print("Supplier updated successfully.")
    view_suppliers(cursor)


def update_clothing_type(connection, cursor):
    """
    Updates the name of a clothing type.
    """
    view_clothing_types(cursor)

    try:
        type_id = int(input("Enter clothing type ID to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    cursor.execute("SELECT * FROM clothing_type WHERE type_id = ?", (type_id,))
    if not cursor.fetchone():
        print("Clothing type not found.")
        return

    new_name = input("Enter new clothing type name: ").strip()
    if not new_name:
        print("Clothing type name cannot be empty.")
        return

    cursor.execute(
        "SELECT * FROM clothing_type WHERE type_name = ?", (new_name,))
    if cursor.fetchone():
        print("Clothing type already exists.")
        return

    cursor.execute(
        "UPDATE clothing_type SET type_name = ? WHERE type_id = ?", (new_name, type_id))
    connection.commit()
    print("Clothing type updated successfully.")
    view_clothing_types(cursor)


def delete_product(connection, cursor):
    view_products(cursor)

    try:
        product_id = int(input("Enter the ID of the product to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    cursor.execute("SELECT 1 FROM product WHERE product_id = ?", (product_id,))
    if not cursor.fetchone():
        print("Product not found.")
        return

    confirm = input(
        "Are you sure you want to delete this product? (y/n): ").lower()
    if confirm == "y":
        cursor.execute(
            "DELETE FROM product WHERE product_id = ?", (product_id,))
        connection.commit()
        print("Product deleted successfully.")
        view_products(cursor)

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
        "SELECT 1 FROM category WHERE category_id = ?", (category_id,))
    if not cursor.fetchone():
        print("Category not found.")
        return

    cursor.execute(
        "SELECT 1 FROM product WHERE category_id = ?", (category_id,))
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
        view_categories(cursor)

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
        "SELECT 1 FROM supplier WHERE supplier_id = ?", (supplier_id,))
    if not cursor.fetchone():
        print("Supplier not found.")
        return

    cursor.execute(
        "SELECT 1 FROM product WHERE supplier_id = ?", (supplier_id,))
    if cursor.fetchone():
        print("Cannot delete supplier. It is used by products.")
        return

    confirm = input(
        "Are you sure you want to delete this supplier? (y/n): ").lower()

    if confirm == "y":
        cursor.execute(
            "DELETE FROM supplier WHERE supplier_id = ?", (supplier_id,))
        connection.commit()
        print("Supplier deleted successfully.")
        view_suppliers(cursor)

    else:
        print("Deletion cancelled.")


def delete_clothing_type(connection, cursor):
    view_clothing_types(cursor)

    try:
        type_id = int(input("Enter the ID of the clothing type to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    cursor.execute("SELECT 1 FROM clothing_type WHERE type_id = ?", (type_id,))
    if not cursor.fetchone():
        print("Clothing type not found.")
        return

    cursor.execute("SELECT 1 FROM product WHERE type_id = ?", (type_id,))
    if cursor.fetchone():
        print("Cannot delete clothing type. It is used by products.")
        return

    confirm = input(
        "Are you sure you want to delete this clothing type? (y/n): ").lower()

    if confirm == "y":
        cursor.execute(
            "DELETE FROM clothing_type WHERE type_id = ?", (type_id,))
        connection.commit()
        print("Clothing type deleted successfully.")
        view_clothing_types(cursor)

    else:
        print("Deletion cancelled.")
