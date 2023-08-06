from django.contrib import admin

# Register your models here.
from gestionPedidos.models import Articulos,Clientes,Pedidos

admin.site.register(Articulos)
admin.site.register(Clientes)
admin.site.register(Pedidos)
