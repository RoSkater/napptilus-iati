from django.forms import ModelForm
from .models import Gorra, Camiseta

class gorraForm(ModelForm):
    class Meta:
        model = Gorra
        fields = ('color1', 'color2', 'color_logo', 'marca', 'unit_price', 'initial_stock', 'description')

class gorraUpdateForm(ModelForm):
    class Meta:
        model = Gorra
        fields = ('color1', 'color2', 'color_logo', 'marca', 'photo', 'unit_price', 'current_stock', 'description')


class camisetaForm(ModelForm):
    class Meta:
        model = Camiseta
        fields = ('color1', 'color2', 'talla', 'marca', 'tejido', 'tallaje', 'mangas', 'unit_price', 'initial_stock', 'description')

class camisetaUpdateForm(ModelForm):
    class Meta:
        model = Camiseta
        fields = ('color1', 'color2', 'talla', 'marca', 'tejido', 'tallaje', 'mangas', 'photo', 'unit_price', 'current_stock', 'description')

