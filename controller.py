"""
Controller module for the Stock Control Database application.

This module acts as the central coordinator between the user interface,
CRUD operations, and application workflow. It receives user menu selections,
routes actions to the appropriate database functions, and manages the
main navigation loop of the application.

Responsibilities:
- Handle user menu navigation
- Route actions to CRUD functions
- Control application flow
- Coordinate communication between modules
"""

from crud import (add_product, add_category, add_supplier, add_clothing_type, update_category, update_clothing_type,
                  update_product,
                  delete_product, delete_category, delete_supplier, delete_clothing_type, update_supplier)
from view import (view_products, view_categories,
                  view_suppliers, view_clothing_types)
from utility import get_choice, warning, error

from reports import show_reports_menu


def handle_action(table_choice, action_choice, connection, cursor):
    """
Dispatches user-selected actions to the appropriate CRUD or view function.

Based on the selected table and action option, this function routes the
request to the corresponding operation such as add, view, update, or delete.
It serves as the main action handler for the application menu system.

Args:
    table_choice (str): User-selected table identifier.
    action_choice (str): User-selected action identifier.
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    if table_choice == "1":  # Product
        if action_choice == "1":
            add_product(connection, cursor)
        elif action_choice == "2":
            view_products(cursor)
        elif action_choice == "3":
            update_product(connection, cursor)
        elif action_choice == "4":
            delete_product(connection, cursor)

    elif table_choice == "2":  # Category
        if action_choice == "1":
            add_category(connection, cursor)
        elif action_choice == "2":
            view_categories(cursor)
        elif action_choice == "3":
            update_category(connection, cursor)
        elif action_choice == "4":
            delete_category(connection, cursor)

    elif table_choice == "3":  # Supplier
        if action_choice == "1":
            add_supplier(connection, cursor)
        elif action_choice == "2":
            view_suppliers(cursor)
        elif action_choice == "3":
            update_supplier(connection, cursor)
        elif action_choice == "4":
            delete_supplier(connection, cursor)

    elif table_choice == "4":  # Clothing Type
        if action_choice == "1":
            add_clothing_type(connection, cursor)
        elif action_choice == "2":
            view_clothing_types(cursor)
        elif action_choice == "3":
            update_clothing_type(connection, cursor)
        elif action_choice == "4":
            delete_clothing_type(connection, cursor)


def run_app(connection, cursor):
    """
Runs the main application loop for the Stock Control Database system.

This function displays the main menu, processes user input, and manages
navigation between database tables and CRUD operations. The loop continues
until the user chooses to exit the application.

Args:
    connection: Active SQLite database connection object.
    cursor: SQLite cursor object used for executing queries.

Returns:
    None
"""
    warning(f"{"="*40}\nWelcome to the Stock Control Database!\n{"="*40}")

    table_choice = ""

    while table_choice != "0":
        table_choice = get_choice("Select table:", [
            "1. Product",
            "2. Category",
            "3. Supplier",
            "4. Clothing Type",
            "5. Reports",
            "0. Exit"])

        if table_choice == "0":
            warning("Exiting the application. Goodbye!")
            break

        elif table_choice == "5":
            show_reports_menu(cursor)

        elif table_choice in ["1", "2", "3", "4"]:
            action_choice = ""
            while action_choice != "5":
                action_choice = get_choice("Select an option:", [
                    "1. Add",
                    "2. View",
                    "3. Update",
                    "4. Delete",
                    "5. Back to Main Menu"
                ])

                if action_choice == "5":
                    break

                handle_action(table_choice, action_choice, connection, cursor)
        else:
            error("Invalid choice. Please select a valid option.")
