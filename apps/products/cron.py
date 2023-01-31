from ..cart.models import OrderProduct

from .models import Product

def check_stock():
    orders = OrderProduct.objects.all()
    productos = Product.objects.all()

    for producto in productos:
        quantity = 0
        for order in orders:
            if order.id == producto.id:
                quantity += order.quantity
        if producto.current_stock + quantity != producto.initial_stock:
            print('Stock readjusment needed for item: ' + producto.id)
            producto.current_stock = producto.initial_stock - quantity
        else:
            print('Stock correct for item: ' + producto.id)

    