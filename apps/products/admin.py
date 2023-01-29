from django.contrib import admin
from .models import Gorra, Camiseta
# Register your models here.

@admin.register(Gorra)
class gorraAdmin(admin.ModelAdmin):
    list_display = ('description','color1','color2','creation_date', 'marca', 'deleted')

@admin.register(Camiseta)
class camisetaAdmin(admin.ModelAdmin):
    list_display = ('description','color1','color2','creation_date', 'marca', 'deleted')

