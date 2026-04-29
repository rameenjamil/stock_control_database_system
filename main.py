from database import connect_db, create_tables
from controller import run_app


if __name__ == "__main__":
    connection, cursor = connect_db()
    create_tables(connection, cursor)
    try:
        run_app(connection, cursor)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()
