import sqlite3 as sqlite

connection = sqlite.connect("db")
local_cursor = connection.cursor()

create_query = open("orders.sql")
sql_string = create_query.read()

def create_table(query):
    data = local_cursor.execute(query)
    return data

def create(order_id, name, drink, size, extras, price):
    create_table(sql_string)
    insert_query = "INSERT INTO orders (order_id,customer_name,drink,size,extras,price) VALUES (?, ?, ?, ?, ?, ?)"

    data = local_cursor.execute(insert_query, (order_id, name, drink, size, extras, price))
    local_cursor.connection.commit()
    print(f"Your order number is: {order_id}\n")
    return data

def get_one(order_id):
    # create_table(create_query)
    select_query = "SELECT * FROM orders WHERE order_id = ?"
    data = local_cursor.execute(select_query, (order_id, ))
    return data

def get():
    select_query = "SELECT * FROM orders"
    data = local_cursor.execute(select_query)
    return data

def update(order_id, param, value):
    update_query = f"""
            UPDATE
                orders
            SET
                {param} = ?
            WHERE
                order_id = ?"""
    data = local_cursor.execute(update_query, (value, order_id))
    local_cursor.connection.commit()
    return data

def update_size(order_id, size, price):
    update_size_query = f"""
            UPDATE
                orders
            SET
                size = ?,
                price = ?
            WHERE
                order_id = ?"""
    data = local_cursor.execute(update_size_query, (size, price, order_id))
    local_cursor.connection.commit()
    return data

def delete_one(order_id):
    delete_query = "DELETE FROM orders WHERE order_id = ?"
    data = local_cursor.execute(delete_query, (order_id, ))
    local_cursor.connection.commit()
    return data

def delete():
    delete_query = "DELETE FROM orders"
    data = local_cursor.execute(delete_query)
    local_cursor.connection.commit()
    return data

# print(local_cursor.execute("SELECT * FROM orders").fetchall())
