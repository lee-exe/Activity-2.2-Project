from controller import create, get_one, get, update, delete_one, delete

print(
    """
    ----------------- Welcome to QA Cafe -------------------
    
    What can we help you with?
    
    1) Add Order
    2) Read Order By ID
    3) Read All Orders
    4) Update Order by ID
    5) Delete Order by ID
    6) Delete All Orders
    """
)

id = input("Please enter a value: ")

if int(id) == 1:
    print(
        """
        ----------------- New Order -------------------
        """)

    name = input("What would you like to order?: ")
    size = input("Please select a size, [Small], [Medium], [Large]: ")
    quantity = input("How many would you like?: ")

    create(name, size, quantity)

elif int(id) == 2:
    print(
        """
        ------------------ View Your Order -------------------
        """)

    order_id = input("Please enter your order number: ")
    get_order = get_one(order_id)
    print(get_order)


elif int(id) == 3:
    print(
        """
        ------------------ View All Orders -------------------
        """)

    get_orders = get()
    print(get_orders)

# Do update last
elif int(id) == 4:
    print(
        """
        ------------------ Update An Order -------------------
        """)

    param_to_update = input("Please state what you would like to update, [name], [size], [quantity]: ")
    new_value = input("Please update what you've selected: ")

    if param_to_update == 'quantity':
        new_value = int(new_value)

    order_id = input("Please enter your order number: ")
    update_order = update(order_id, param_to_update, new_value)





elif int(id) == 5:
    print(
        """
        ------------------ Cancel An Order -------------------
        """)

    order_id = input("Please enter your order ID: ")
    delete_order = delete_one(order_id)
    print(f"Order {order_id} has been cancelled.")

elif int(id) == 6:
    print(
        """
        ------------------ Cancel All Orders -------------------
        """)

    delete_orders = delete()
    print("All orders have been cancelled.")
