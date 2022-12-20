import service
from order import order
import string
import shortuuid

def create(name, size, quantity):
    # orders = service.create(order)
    # return orders

    alphabet = string.ascii_lowercase + string.digits
    su = shortuuid.ShortUUID(alphabet=alphabet)

    new_order = order(su.random(length=16), name, size, quantity)
    orders = service.create(new_order.order_id, new_order.name, new_order.size, new_order.quantity)
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

def delete_one(order_id):
    delete_order = service.delete_one(order_id)
    return delete_order


def delete():
    delete_all = service.delete()
    return delete_all.fetchall()

