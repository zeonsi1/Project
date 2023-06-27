from django.contrib import admin
from .models import producto, carrito, producto_carrito, tipoUsuario, region, comuna, usuario
# Register your models here.

admin.site.register(producto)
admin.site.register(carrito)
admin.site.register(producto_carrito)
admin.site.register(tipoUsuario)
admin.site.register(region)
admin.site.register(comuna)
admin.site.register(usuario)