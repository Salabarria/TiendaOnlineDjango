from django.contrib import admin

# Register your models here.
from gestionPedidos.models import Articulos,Clientes,Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","tfno")  # muesta estos campos en el panel de control del modelo cliente
    search_fields=("nombre","tfno")                            # realiza una busqueda pro nombre en el campo que se implementada
    list_filter=("nombre","email")
    
class ArticulosAdmin(admin.ModelAdmin):                # muesta estos campos en el panel de control del modelo Articulos
    list_display=("nombre","seccion","precio")
    search_fields=("nombre","precio")
    list_filter=("precio",)
    

class PedidosAdmin(admin.ModelAdmin):                 # muesta estos campos en el panel de control del modelo Pedidos
    list_display=("numero","fecha","entregado")   
    search_fields=("entregado","fecha") 
    list_filter=("fecha","entregado")


# Register your models here.
admin.site.register(Articulos,ArticulosAdmin)   
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Pedidos,PedidosAdmin)



