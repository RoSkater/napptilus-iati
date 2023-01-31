from django.db import models

from apps.products.models import Product

# Create your models here.

class OrderProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product.id)

class Cart(models.Model):
    products = models.ManyToManyField(OrderProduct)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.products.all()

    def get_cart_total(self):
        return sum([item.product.unit_price*item.quantity for item in self.products.all()])
