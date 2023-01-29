import datetime

from django.db import models

# Create your models here.

class Product(models.Model):
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    creation_date = models.DateField(default = datetime.datetime.now)
    photo = models.ImageField(upload_to='images/')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    initial_stock = models.IntegerField()
    current_stock = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False, null=False)
    
    def initial_current_stock(self):
        self.current_stock = self.initial_stock

class Gorra(Product):
    color_logo = models.CharField(max_length=50)

class Camiseta(Product):
    talla = models.CharField(max_length=4)
    tejido = models.CharField(max_length=50)
    tallaje = models.CharField(max_length=50)
    mangas = models.BooleanField(default=True, null=True)


