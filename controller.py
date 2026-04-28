from crud import (add_product, add_category, add_supplier, add_clothing_type,
                  update_product,
                  delete_product, delete_category, delete_supplier, delete_clothing_type)
from view import (view_products, view_categories,
                  view_suppliers, view_clothing_types)


def get_choice(prompt, options):
    print(f"\n{prompt}")
    for option in options:
        print(option)

    choice = input("Choose an option: ")
    return choice


def handle_action(table_choice, action_choice, connection, cursor):
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
            print("Update not available for categories.")
        elif action_choice == "4":
            delete_category(connection, cursor)

    elif table_choice == "3":  # Supplier
        if action_choice == "1":
            add_supplier(connection, cursor)
        elif action_choice == "2":
            view_suppliers(cursor)
        elif action_choice == "3":
            print("Update not available for suppliers.")
        elif action_choice == "4":
            delete_supplier(connection, cursor)

    elif table_choice == "4":  # Clothing Type
        if action_choice == "1":
            add_clothing_type(connection, cursor)
        elif action_choice == "2":
            view_clothing_types(cursor)
        elif action_choice == "3":
            print("Update not available for clothing types.")
        elif action_choice == "4":
            delete_clothing_type(connection, cursor)


def run_app(connection, cursor):
    print(f"{"="*40}\nWelcome to the Stock Control Database!\n{"="*40}")

    table_choice = ""

    while table_choice != "5":
        table_choice = get_choice("Select table:", [
            "1. Product",
            "2. Category",
            "3. Supplier",
            "4. Clothing Type",
            "5. Exit"])

        if table_choice == "5":
            print("Exiting the application. Goodbye!")

        elif table_choice in ["1", "2", "3", "4"]:
            action_choice = get_choice("Select Table:", [
                "1. Add",
                "2. View",
                "3. Update",
                "4. Delete",
                "5. Back to Main Menu"
            ])

            if action_choice == "5":
                handle_action(table_choice, action_choice, connection, cursor)
        else:
            print("Invalid choice. Please select a valid option.")
