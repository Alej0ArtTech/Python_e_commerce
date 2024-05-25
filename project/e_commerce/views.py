from django.urls import path
from . import views
from django.shortcuts import render
from .models import Producto, Pedido, Categoria

def index(request):
    return render(request, 'index.html')

def producto(request):
    return render(request, 'producto.html')

def categoria(request):
    return render(request, 'categoria.html')

def pedido(request):
    return render(request, 'pedido.html')

def guardar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        # Crea una instancia del modelo Producto y guarda los datos en la base de datos
        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
        producto.save()
        return render(request, 'index.html')

def guardar_pedido(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        producto = request.POST.get('producto')
        estado = request.POST.get('estado')

        # Crear una instancia del modelo Pedido y guardar los datos en la base de datos
        pedido = Pedido(nombre=nombre, apellido=apellido, producto=producto, estado=estado)
        pedido.save()

    # No hay necesidad de pasar productos al contexto de la plantilla
    return render(request, 'index.html')


def busqueda_producto(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        try:
            product = Producto.objects.get(nombre=product_name)
            return render(request, 'index.html', {'product': product})
        except Producto.DoesNotExist:
            return render(request, 'index.html', {'error': 'Product not found'})
    return render(request, 'index.html')

def guardar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        # Crea una instancia del modelo Categoria y guarda los datos en la base de datos
        categoria = Categoria(nombre=nombre, descripcion=descripcion)
        categoria.save()
        return render(request, 'index.html')