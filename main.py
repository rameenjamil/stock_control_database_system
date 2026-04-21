from database import connect_db, create_tables
from crud import add_product, add_category, add_supplier, add_clothing_type, update_product, delete_product
from view import view_products, view_categories, view_suppliers, view_clothing_types


def main_menu():
    print("\nSelect table:")
    print("1. Product")
    print("2. Category")
    print("3. Supplier")
    print("4. Clothing Type")
    print("5. Exit")


def action_menu():
    print("\nSelect action:")
    print("1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")


def run_app(connection, cursor):

    print("Welcome to the Stock Control Database")

    is_running = True

    while is_running:
        main_menu()
        table_choice = input("Choose table: ")

        if table_choice == "5":
            print("Exiting...")
            is_running = False
            continue

        action_menu()
        action_choice = input("Choose action: ")

        # PRODUCT
        if table_choice == "1":
            if action_choice == "1":
                add_product(connection, cursor)
            elif action_choice == "2":
                view_products(cursor)
            elif action_choice == "3":
                update_product(connection, cursor)
            elif action_choice == "4":
                delete_product(connection, cursor)

        # CATEGORY
        elif table_choice == "2":
            if action_choice == "1":
                add_category(connection, cursor)
            elif action_choice == "2":
                view_categories(cursor)

        # SUPPLIER
        elif table_choice == "3":
            if action_choice == "1":
                add_supplier(connection, cursor)
            elif action_choice == "2":
                view_suppliers(cursor)

        # CLOTHING TYPE
        elif table_choice == "4":
            if action_choice == "1":
                add_clothing_type(connection, cursor)
            elif action_choice == "2":
                view_clothing_types(cursor)

        else:
            print("Invalid choice.")


connection, cursor = connect_db()
create_tables(connection, cursor)

run_app(connection, cursor)

connection.close()
