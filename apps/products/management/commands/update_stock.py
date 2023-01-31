import os

from pathlib import Path

from django.core.management.base import BaseCommand

from apps.products.models import Product

from apps.cart.models import OrderProduct

BASE_DIR = Path(__file__).resolve().parent

class Command(BaseCommand):
    def handle(self, *args, **options):
        orders = OrderProduct.objects.all()
        productos = Product.objects.all()

        fich = os.path.join(BASE_DIR, 'log.txt')

        for producto in productos:
            print(f'PRODUCTO {producto.id} Current Stock: {producto.current_stock}')
            quantity = 0
            for order in orders:
                print(f'ORDER {order.product.id} Cantidad: {order.quantity}')
                if int(order.product.id) == int(producto.id):
                    quantity += (order.quantity)
            if producto.current_stock + quantity != producto.initial_stock:
                with open(fich, 'a') as file:
                    file.write('Stock readjusment needed for item: ' + str(producto.id) + "\n")
                
                producto.current_stock = producto.initial_stock - quantity
            else:
                with open(fich, 'a') as file:
                    file.write('Stock readjusment needed for item: ' + str(producto.id) + "\n")
