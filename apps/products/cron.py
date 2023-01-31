import os
from django.core.management import call_command
from pathlib import Path
from django_cron import CronJobBase, Schedule
from ..cart.models import OrderProduct
from .models import Product

BASE_DIR = Path(__file__).resolve().parent

class UpdateStock(CronJobBase):

    schedule = Schedule(run_every_mins=0.0833)
    code = 'apps.products.update_stock'

    def do(self):
        orders = list(OrderProduct.objects.values())
        productos = list(Product.objects.values())

        print(orders)

        fich = os.path.join(BASE_DIR, 'log.txt')

        for producto in productos:

            p_id = producto['id']
            p_cs = producto['current_stock']
            p_is = producto['initial_stock']
            print(f'PRODUCTO {p_id} Current Stock: {p_cs} Initial Stock: {p_is}')
            quantity = 0

            for order in orders:
                o_id = order['product_id']
                o_quant = order['quantity']
                print(f'ORDER {o_id} Cantidad: {o_quant}')
                if o_id == p_id:
                    print('EQUALS')
                    quantity += o_quant
                    print(f'QUANTITY = {quantity}')
            total = p_cs + quantity
            print(f'TOTAL = {total}')
  
            if total == p_is:
                
                with open(fich, 'a') as file:
                    file.write('Stock is OK for product: ' + str(p_id) + "\n")
            else:
                with open(fich, 'a') as file:
                    file.write('Stock readjusment needed for item: ' + str(p_id) + "\n")
                
                p_cs = p_is - quantity

                prod = Product.objects.get(id=p_id)
                prod.current_stock = p_cs
                prod.save()

        #call_command('update_stock')
        

    