from django import forms
from .models import Producto, Categoria, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imagen']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'ciudad', 'telefono']

class BusquedaProductoForm(forms.Form):
    nombre = forms.CharField(label='Buscar producto por nombre', max_length=100)
