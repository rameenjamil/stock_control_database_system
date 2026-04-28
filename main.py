from database import connect_db, create_tables
from controller import run_app


connection, cursor = connect_db()
create_tables(connection, cursor)

run_app(connection, cursor)

connection.close()
