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
        return render(request, 'producto.html')

def guardar_pedido(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        productos_ids = request.POST.getlist('productos')
        estado = request.POST.get('estado')

        # Obtener los objetos Producto basados en sus IDs
        productos = Producto.objects.filter(id__in=productos_ids)

        # Crear una instancia del modelo Pedido y guardar los datos en la base de datos
        pedido = Pedido(cliente=cliente, estado=estado)
        pedido.save()
        pedido.producto.set(productos)


    productos = Producto.objects.all()
    return render(request, 'formulario_pedido.html', {'productos': productos})

def guardar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        # Crea una instancia del modelo Categoria y guarda los datos en la base de datos
        categoria = Categoria(nombre=nombre, descripcion=descripcion)
        categoria.save()
        return render(request, 'formulario_categoria.html')