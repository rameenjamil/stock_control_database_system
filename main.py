
from database import connect_db, create_tables
from crud import add_product, add_category, add_supplier


conn, cursor = connect_db()
create_tables(conn, cursor)

add_product(conn, cursor)
add_category(conn, cursor)
add_supplier(conn, cursor)
