"""
CRUD operations module for the Stock Control Database application.

This module contains all Create, Read, Update, and Delete operations
for products, categories, suppliers, and clothing types. It manages
user input validation, database transactions, and data integrity.

Responsibilities:
- Insert new records into the database
- Update existing records
- Delete records safely
- Validate user input
- Handle database transactions
- Provide interactive selection menus
"""

import sqlite3
from utility import get_choice, is_valid_name, error, warning, success
from view import view_categories, view_suppliers, view_products, view_clothing_types


def select_from_table(cursor, table, id_col, name_col):
    """
Displays records from a database table and allows the user to select one.

This helper function retrieves IDs and display names from the specified
table, presents them as a numbered list, and returns the selected record ID.
It is commonly used in update and delete operations.

Args:
    cursor: SQLite cursor object used for executing queries.
    table (str): Name of the database table.
    id_col (str): Name of the ID column.
    name_col (str): Name of the display column.

Returns:
    int | None:
        Returns the selected record ID, or None if the user cancels.
"""
    cursor.execute(f"SELECT {id_col}, {name_col} FROM {table}")
    rows = cursor.fetchall()

    if not rows:
        error(f"\nNo records found in {table.replace('_', ' ')}.")
        return None

    print(f"\nSelect {table.replace('_', ' ').title()} (0 to cancel):")

    for i, row in enumerate(rows, start=1):
        print(f"{i}. {row[1]}")

    choice = None

    while choice is None:
        try:
            user_input = input("Choose an option (0 to cancel): ")

            if user_input == "0":
                return None

            number = int(user_input)

            if 1 <= number <= len(rows):
                choice = number
            else:
                error("Invalid choice. Please select from the list.")

        except ValueError:
            error("Invalid input. Please enter a number.")

    return rows[choice - 1][0]


def add_product(connection, cursor):
    """
Adds a new product record to the database.

This function collects product information from the user, validates
all required inputs, and inserts the new product into the product table.
It also allows the user to select related category, supplier, and
clothing type records.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    category_id = select_from_table(
        cursor, "category", "category_id", "category_name")
    if category_id is None:
        return

    supplier_id = select_from_table(
        cursor, "supplier", "supplier_id", "supplier_name")
    if supplier_id is None:
        return

    type_id = select_from_table(
        cursor, "clothing_type", "type_id", "type_name")
    if type_id is None:
        return

    name = input("Enter product name: ").strip()

    if not name or not is_valid_name(name):
        error("Invalid product name. Please enter a valid name.")
        return

    size = input("Enter product size: ").strip()

    try:
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))
    except ValueError:
        error("Invalid input. Please enter the correct datatype.")
        return

    cursor.execute("""
                   INSERT INTO product (name, size, quantity, price, category_id, supplier_id, type_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, size, quantity, price, category_id, supplier_id, type_id))

    connection.commit()
    success(f"\nProduct added successfully.")


def add_category(connection, cursor):
    """
Adds a new category to the database.

This function validates the category name, checks for duplicate entries,
and inserts the category into the database if the input is valid.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    category_name = input("Enter category name: ").strip()

    if not category_name or not is_valid_name(category_name):
        error("Invalid category name. Please enter a valid name.")
        return

    # checking for duplicates
    cursor.execute(
        "SELECT 1 FROM category WHERE category_name = ?", (category_name,))
    if cursor.fetchone():
        warning("Category already exists.")
        return

    cursor.execute("INSERT INTO category (category_name) VALUES (?)",
                   (category_name,))  # comma is needed because it is a tuple

    connection.commit()
    success(f"\nCategory added successfully.")


def add_supplier(connection, cursor):
    """
Adds a new supplier record to the database.

This function collects supplier information, validates the input,
checks for duplicate supplier names, and stores the new supplier
in the supplier table.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""

    supplier_name = input("Enter supplier name: ").strip()
    contact_info = input("Enter contact info: ").strip()

    if not supplier_name or not is_valid_name(supplier_name):
        error("Invalid supplier name.")
        return

    # checking for duplicates
    cursor.execute(
        "SELECT 1 FROM supplier WHERE supplier_name = ?", (supplier_name,))
    if cursor.fetchone():
        warning("Supplier already exists.")
        return

    cursor.execute("INSERT INTO supplier (supplier_name, contact_info)VALUES (?, ?)",
                   (supplier_name, contact_info))

    connection.commit()
    success("\nSupplier added successfully.")


def add_clothing_type(connection, cursor):
    """
Adds a new clothing type to the database.

This function validates the clothing type name, ensures no duplicate
records exist, and inserts the new clothing type into the database.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    type_name = input("Enter clothing type name: ").strip()

    if not type_name:
        error("Clothing type name cannot be empty.")
        return

    # checking for duplicates
    cursor.execute(
        "SELECT 1 FROM clothing_type WHERE type_name = ?", (type_name,))
    if cursor.fetchone():
        warning("Clothing type already exists.")
        return

    cursor.execute("""
                   INSERT INTO clothing_type (type_name)
        VALUES (?)
    """, (type_name,))

    connection.commit()
    success("\nClothing type added successfully.")


def update_product(connection, cursor):
    """
Updates a selected field of an existing product.

This function allows the user to select a product and modify one
of its editable attributes such as name, size, quantity, or price.
The updated information is saved immediately to the database.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    view_products(cursor)

    product_id = select_from_table(cursor, "product", "product_id", "name")
    if product_id is None:
        return

# mapping of user choices to database columns and data types
    fields = {
        "1": ("Name", "name", str),
        "2": ("Size", "size", str),
        "3": ("Quantity", "quantity", int),
        "4": ("Price", "price", float)
    }

    # prompt user to select which field to update
    choice = get_choice("Select field to update:", [
        "1. Name",
        "2. Size",
        "3. Quantity",
        "4. Price"
    ])

    # get the corresponding column name and data type based on user choice
    label, column, data_type = fields[choice]

    valid = False
    while not valid:
        try:
            new_value = data_type(
                input(f"Enter new {label.lower()}: ").strip())
            valid = True
        except ValueError:
            error("Invalid input type.")

    cursor.execute(
        f"UPDATE product SET {column} = ? WHERE product_id = ?",
        (new_value, product_id)
    )

    connection.commit()
    success("Product updated successfully.")

    # fetch updated record to show user
    cursor.execute("SELECT * FROM product WHERE product_id = ?", (product_id,))
    updated = cursor.fetchone()

    if updated:
        warning("\nUpdated Product:")
        print(f"""
        ID: {updated[0]}
        Name: {updated[1]}
        Size: {updated[2]}
        Quantity: {updated[3]}
        Price: {updated[4]}""")


def update_category(connection, cursor):
    """
Updates the name of an existing category.

This function displays available categories, allows the user to
select one, validates the new category name, and updates the record
in the database.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    view_categories(cursor)

    category_id = select_from_table(
        cursor, "category", "category_id", "category_name")
    if category_id is None:
        return

    new_name = input("Enter new category name: ").strip()
    if not new_name:
        error("Category name cannot be empty.")
        return

    cursor.execute(
        "SELECT 1 FROM category WHERE category_name = ?", (new_name,))
    if cursor.fetchone():
        warning("Category name already exists.")
        return

    cursor.execute("UPDATE category SET category_name = ? WHERE category_id = ?",
                   (new_name, category_id))
    connection.commit()
    success("Category updated successfully.")
    view_categories(cursor)


def update_supplier(connection, cursor):
    """
Updates supplier information in the database.

This function allows the user to modify either the supplier name
or the supplier contact information. Input validation and duplicate
checks are performed where necessary.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    view_suppliers(cursor)

    supplier_id = select_from_table(
        cursor, "supplier", "supplier_id", "supplier_name")
    if supplier_id is None:
        return

    warning("""
        What would you like to update?
        1. Name
        2. Contact Info
        """)
    choice = input("Enter choice: ")

    if choice == "1":
        new_value = input("Enter new supplier name: ").strip()
        if not new_value:
            error("Supplier name cannot be empty.")
            return
        cursor.execute(
            "SELECT 1 FROM supplier WHERE supplier_name = ?", (new_value,))
        if cursor.fetchone():
            warning("Supplier already exists.")
            return
        column = "supplier_name"

    elif choice == "2":
        new_value = input("Enter new contact info: ").strip()
        column = "contact_info"

    else:
        error("Invalid choice.")
        return

    cursor.execute(f"UPDATE supplier SET {column} = ? WHERE supplier_id = ?",
                   (new_value, supplier_id))
    connection.commit()
    success("Supplier updated successfully.")
    view_suppliers(cursor)


def update_clothing_type(connection, cursor):
    """
Updates the name of an existing clothing type.

This function allows the user to select a clothing type, validate
a new name, and apply the update to the database.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    view_clothing_types(cursor)

    type_id = select_from_table(
        cursor, "clothing_type", "type_id", "type_name")
    if type_id is None:
        return

    type_name = input("Enter new clothing type name: ").strip()
    if not type_name:
        error("Clothing type name cannot be empty.")
        return

    if not is_valid_name(type_name):
        error("Invalid clothing type name.")
        return

    cursor.execute(
        "SELECT 1 FROM clothing_type WHERE type_name = ?", (type_name,))
    if cursor.fetchone():
        warning("Clothing type already exists.")
        return

    cursor.execute(
        "UPDATE clothing_type SET type_name = ? WHERE type_id = ?", (type_name, type_id))
    connection.commit()
    success("Clothing type updated successfully.")
    view_clothing_types(cursor)


def delete_product(connection, cursor):
    """
Deletes a product record from the database.

This function displays available products, allows the user to select
one for deletion, and requests confirmation before permanently removing
the product record.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    view_products(cursor)
    product_id = select_from_table(cursor, "product", "product_id", "name")
    if product_id is None:
        return

    confirm = input(
        "Are you sure you want to delete this product? (y/n): ").lower()
    if confirm == "y":
        cursor.execute(
            "DELETE FROM product WHERE product_id = ?", (product_id,))
        connection.commit()
        success("Product deleted successfully.")
        view_products(cursor)

    else:
        error("Deletion cancelled.")


def delete_category(connection, cursor):
    """
Deletes a category record from the database.

This function allows the user to select a category for deletion and
handles potential database integrity errors caused by foreign key
constraints.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    view_categories(cursor)

    category_id = select_from_table(
        cursor, "category", "category_id", "category_name")
    if category_id is None:
        return

    confirm = input(
        "Are you sure you want to delete this category? (y/n): ").lower()

    if confirm == "y":
        try:
            cursor.execute(
                "DELETE FROM category WHERE category_id = ?", (category_id,))
            connection.commit()
            success("Category deleted successfully.")
            view_categories(cursor)
        except sqlite3.IntegrityError:
            warning("Cannot delete category. It is used by existing products.")
    else:
        error("Deletion cancelled.")


def delete_supplier(connection, cursor):
    """
Deletes a supplier record from the database.

This function displays available suppliers, confirms the deletion,
and safely removes the selected supplier while handling database
constraint errors.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    view_suppliers(cursor)

    supplier_id = select_from_table(
        cursor, "supplier", "supplier_id", "supplier_name")
    if supplier_id is None:
        return

    confirm = input(
        "Are you sure you want to delete this supplier? (y/n): ").lower()
    if confirm == "y":
        try:
            cursor.execute(
                "DELETE FROM supplier WHERE supplier_id = ?", (supplier_id,))
            connection.commit()
            success("Supplier deleted successfully.")
            view_suppliers(cursor)
        except sqlite3.IntegrityError:
            warning(f"Cannot delete the supplier. It is used by existing products.")

    else:
        error("Deletion cancelled.")


def delete_clothing_type(connection, cursor):
    """
Deletes a clothing type record from the database.

This function allows the user to remove a clothing type after
confirmation. Database integrity checks are handled to prevent
invalid deletions.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    view_clothing_types(cursor)

    type_id = select_from_table(
        cursor, "clothing_type", "type_id", "type_name")
    if type_id is None:
        return

    confirm = input(
        "Are you sure you want to delete this clothing type? (y/n): ").lower()

    if confirm == "y":
        try:
            cursor.execute(
                "DELETE FROM clothing_type WHERE type_id = ?", (type_id,))
            connection.commit()
            success("Clothing type deleted successfully.")
            view_clothing_types(cursor)
        except sqlite3.IntegrityError:
            warning("Cannot delete clothing type. It is used by existing products.")

    else:
        error("Deletion cancelled.")
