from django.db import models
# Este curioso import hace uso de un tal USER pregconfigurado en django
from django.contrib.auth.models import User

# Create your models here.

#    imagen = models.ImageField(upload_to='productos/')
# la imagen la ncoporamos si da ttiempo

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Pedido(models.Model):
    nombre = models.CharField(max_length=255, default="Sin cliente")
    apellido = models.CharField(max_length=255, default="Sin apellido")
    producto = models.CharField(max_length=255, null= False, default="Sin apellido") #ManyToManyField(Producto)  # Cambiado a ManyToManyField para permitir múltiples productos
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cliente} - {self.fecha_pedido}"