from django.contrib import admin
from .models import Categoria, Producto, Cliente

# Registro de modelos en el admin
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
