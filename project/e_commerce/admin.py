from django.contrib import admin

# Register your models here.
from .models import Pedido, Categoria, Producto


admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Producto)