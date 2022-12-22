from controller import create, get_one, get, update, update_size, delete_one, delete
from utils import calculate_price
def options():
    print(
        """
        ----------------- Welcome to QA Cafe -------------------

        What can we help you with?

        1) View Menu
        2) Add Order
        3) Read Order By ID
        4) Read All Orders
        5) Update Order by ID
        6) Delete Order by ID
        7) Delete All Orders
        """
    )

options()
id = input("Please enter a value: ")

if int(id) == 1:
    print(
        """
        ----------------- Menu -------------------
        
        Base Drinks
        
        1) Americano
        2) Latte
        3) Espresso
        4) Hot Chocolate
        5) Cappuccino
        6) English Tea
        
        Sizes
        
        1) Small    £1.20
        2) Medium   £1.80
        3) Large    £2.30
        
        """)

elif int(id) == 2:
    print(
        """
        ----------------- New Order -------------------
        """)

    name = input("Please enter your name: ")
    drink = input("What would you like to order? ")
    size = input("Please select a size, [Small], [Medium], [Large]: ")
    extras = input("Any extras (Skip if none): ")
    # extras = user_input.split(", ")
    price = float(calculate_price(size))

    create(name, drink, size, extras, price)

elif int(id) == 3:
    print(
        """
        ------------------ View Your Order -------------------
        """)

    order_id = input("Please enter your order number: ")
    get_order = get_one(order_id)
    print(get_order)

elif int(id) == 4:
    print(
        """
        ------------------ View All Orders -------------------
        """)

    get_orders = get()
    print(get_orders)

elif int(id) == 5:
    print(
        """
        ------------------ Update An Order -------------------
        """)

    param_to_update = input("Please state what you would like to update, [drink], [size], [extras]: ")
    new_value = input("Please update what you've selected: ")
    order_id = input("Please enter your order number: ")

    if param_to_update == 'size':
        new_price = float(calculate_price(new_value))
        update_order = update_size(order_id, new_value, new_price)
    else:
        update_order = update(order_id, param_to_update, new_value)

elif int(id) == 6:
    print(
        """
        ------------------ Cancel An Order -------------------
        """)

    order_id = input("Please enter your order ID: ")
    delete_order = delete_one(order_id)
    print(f"Order {order_id} has been cancelled.")

elif int(id) == 7:
    print(
        """
        ------------------ Cancel All Orders -------------------
        """)

    delete_orders = delete()
    print("All orders have been cancelled.")
