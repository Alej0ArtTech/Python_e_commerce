from django.db import models
# Este curioso import hace uso de un tal USER pregconfigurado en django
from django.contrib.auth.models import User

# Create your models here.



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    productos = models.ManyToManyField(Producto)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)
