
from database import connect_db, create_tables
from crud import add_product, add_category, add_supplier, add_clothing_type
from view import view_products, view_categories, view_suppliers, view_clothing_types


connection, cursor = connect_db()
create_tables(connection, cursor)

add_category(connection, cursor)
add_supplier(connection, cursor)
add_product(connection, cursor)

view_products(cursor)
view_categories(cursor)
view_suppliers(cursor)
view_clothing_types(cursor)

connection.close()
