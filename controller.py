import service
from order import order
import string
import shortuuid

def create(name, drink, size, extras, price):
    alphabet = string.ascii_lowercase + string.digits
    su = shortuuid.ShortUUID(alphabet=alphabet)

    new_order = order(su.random(length=16), name, drink, size, extras, price)
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
    get_order = service.get_one(order_id)
    return get_order.fetchall()

def get():
    get_orders = service.get()
    return get_orders.fetchall()

def update(order_id, param, value):
    update_order = service.update(order_id, param, value)
    return update_order.fetchall()

def update_size(order_id, size, price):
    update_order = service.update_size(order_id, size, price)
    return update_order.fetchall()


def delete_one(order_id):
    delete_order = service.delete_one(order_id)
    return delete_order

def delete():
    delete_all = service.delete()
    return delete_all.fetchall()
