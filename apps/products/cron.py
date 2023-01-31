import os
from pathlib import Path
from ..cart.models import OrderProduct
from .models import Product

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def update_stock():
    orders = list(OrderProduct.objects.values())
    productos = list(Product.objects.values())

    fich = os.path.join(BASE_DIR, 'cron.log')

    for producto in productos:

        p_id = producto['id']
        p_cs = producto['current_stock']
        p_is = producto['initial_stock']
        quantity = 0

        for order in orders:
            o_id = order['product_id']
            o_quant = order['quantity']
            if o_id == p_id:
                quantity += o_quant
        total = p_cs + quantity

        if total == p_is:
            
            with open(fich, 'a') as file:
                file.write('Stock is OK for product: ' + str(p_id) + "\n")
        else:
            with open(fich, 'a') as file:
                file.write('Stock readjusment needed for item: ' + str(p_id) + "\n")
            
            p_cs = p_is - quantity
                
            with open(fich, 'a') as file:
                file.write('Stock fixed for item: ' + str(p_id) + "\n")
            

            prod = Product.objects.get(id=p_id)
            prod.current_stock = p_cs
            prod.save()
    

    