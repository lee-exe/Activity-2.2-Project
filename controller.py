"""
The controller manages the input and decides which
service to send the incoming data to
"""
import string
import shortuuid
import service
from order import order


def create(name, drink, size, extras, price):
    """
    Control for creating a new order
    :param name: name of customer
    :param drink: drink type
    :param size: size of drink
    :param extras: any extras or toppings
    :param price: price based on size
    :return: returns new order object
    """
    alphabet = string.ascii_lowercase + string.digits
    short_uuid = shortuuid.ShortUUID(alphabet=alphabet)

    new_order = order(short_uuid.random(length=16), name, drink, size, extras, price)
    orders = service.create(
        new_order.order_id,
        new_order.customer_name,
        new_order.drink,
        new_order.size,
        new_order.extras,
        new_order.price
    )
    return orders

def get_one(order_id):
    """
    Returns single order
    :param order_id:
    :return:
    """
    get_order = service.get_one(order_id)
    return get_order.fetchall()

def get():
    """
    Returns all orders
    :return:
    """
    get_orders = service.get()
    return get_orders.fetchall()

def update(order_id, param, value):
    """
    Updates an order
    :param order_id:
    :param param: what needs updating
    :param value: new values
    :return: updated order
    """
    update_order = service.update(order_id, param, value)
    return update_order.fetchall()

def update_size(order_id, size, price):
    """
    Separate controller for changing the price
    based on the size
    :param order_id:
    :param size: new size
    :param price: new price
    :return:
    """
    update_order = service.update_size(order_id, size, price)
    return update_order.fetchall()


def delete_one(order_id):
    """
    Deletes a single order
    :param order_id:
    :return:
    """
    delete_order = service.delete_one(order_id)
    return delete_order

def delete():
    """
    Deletes all orders
    :return:
    """
    delete_all = service.delete()
    return delete_all.fetchall()
