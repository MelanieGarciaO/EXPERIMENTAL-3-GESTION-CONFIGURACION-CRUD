from django import forms
from .models import Producto, Marca

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'marca']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['marca'].queryset = Marca.objects.filter(eliminado=False)

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']