import sqlite3 as sqlite


connection = sqlite.connect("db")

local_cursor = connection.cursor()

admin_query = "SELECT * FROM sqlite_master"
create_query = "CREATE TABLE IF NOT EXISTS orders(" \
               "order_id VARCHAR(16) NOT NULL," \
               "name VARCHAR(25)," \
               "size VARCHAR(10)," \
               "quantity int," \
               "PRIMARY KEY(order_id)" \
               ")"

show_query = "SELECT * FROM sqlite_master WHERE type='table' AND name='orders'"
# delete_query = "DROP TABLE if EXISTS orders"
check_table_query = "SELECT * FROM orders"

def create_table(query):
    data = local_cursor.execute(query)
    return data

# def check_table_exists(query):
#     data = local_cursor.execute(query)
#     return data

def create(order_id, name, size, quantity):
    create_table(create_query)
    insert_query = "INSERT INTO orders (order_id,name,size,quantity) VALUES (?, ?, ?, ?)"


    data = local_cursor.execute(insert_query, (order_id, name, size, quantity))
    local_cursor.connection.commit()
    print(f"Your order number is: {order_id}")
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



print(local_cursor.execute("SELECT * FROM orders").fetchall())
# create_table(create_query)
# print(create(create_query))
# print(local_cursor.execute("SELECT * FROM db.sqlite_master WHERE type='table'"))




