from django.shortcuts import render, redirect
from .forms import ProductoForm, CategoriaForm, ClienteForm, BusquedaProductoForm
from .models import Producto

#----- Agregar Producto -----

def agregar_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('agregar_producto')
    else:
        formulario = ProductoForm()
    
    return render(request, 'tienda/agregar_producto.html', {'formulario': formulario})

#----- Agregar Categoria -----

def agregar_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('agregar_categoria')
    else:
        formulario = CategoriaForm()
    
    return render(request, 'tienda/agregar_categoria.html', {'formulario': formulario})

#----- Agregar Cliente -----

def agregar_cliente(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('agregar_cliente')
    else:
        formulario = ClienteForm()
    
    return render(request, 'tienda/agregar_cliente.html', {'formulario': formulario})

#----- Buscar producto -----

def buscar_producto(request):
    resultados = []
    formulario = BusquedaProductoForm()

    if request.method == 'GET' and 'nombre' in request.GET:
        formulario = BusquedaProductoForm(request.GET)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            resultados = Producto.objects.filter(nombre__icontains=nombre)

    return render(request, 'tienda/buscar_producto.html', {
        'formulario': formulario,
        'resultados': resultados
    })