from django.forms import ModelForm
from .models import Gorra, Camiseta

class gorraForm(ModelForm):
    class Meta:
        model = Gorra
        fields = ('color1', 'color2', 'color_logo', 'marca', 'unit_price', 'initial_stock', 'description', 'photo')

class gorraUpdateForm(ModelForm):
    class Meta:
        model = Gorra
        fields = ('color1', 'color2', 'color_logo', 'marca', 'unit_price', 'current_stock', 'description', 'photo')


class camisetaForm(ModelForm):
    class Meta:
        model = Camiseta
        fields = ('color1', 'color2', 'talla', 'marca', 'tejido', 'tallaje', 'mangas', 'unit_price', 'initial_stock', 'description', 'photo')

class camisetaUpdateForm(ModelForm):
    class Meta:
        model = Camiseta
        fields = ('color1', 'color2', 'talla', 'marca', 'tejido', 'tallaje', 'mangas', 'unit_price', 'current_stock', 'description', 'photo')

