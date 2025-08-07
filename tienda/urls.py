from django.urls import path
from . import views

urlpatterns = [
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),
]
