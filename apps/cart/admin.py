from django.contrib import admin

from .models import OrderProduct, Cart

# Register your models here.

@admin.register(Cart)
class cartAdmin(admin.ModelAdmin):
    list_display = ('date_ordered',)

@admin.register(OrderProduct)
class gorraAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
