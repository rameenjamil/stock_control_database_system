from database import connect_db, create_tables
from controller import run_app
from colorama import init
from utility import error

init()


if __name__ == "__main__":
    connection, cursor = connect_db()
    create_tables(connection, cursor)
    try:
        run_app(connection, cursor)
    except Exception as e:
        error(f"An error occurred: {e}")
    finally:
        connection.close()
