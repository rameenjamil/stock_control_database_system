"""
Main entry point for the Stock Control Database application.

This module initializes the database connection, creates required
tables, and starts the main application loop. It also handles
unexpected runtime errors and ensures the database connection
is properly closed when the application exits.
"""

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
