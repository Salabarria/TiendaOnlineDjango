from django.test import TestCase

# Create your tests here.
from gestionPedidos.models import Articulos,Clientes,Pedidos

def jsdfhsk():
    elem1 = Articulos.objects.create(name="mesa",seccion="decoracion",precio=90) # esta es una manera de insertar elementos en la tabla
    
    elem2 =  Articulos(name="camisa",seccion="confeccion",precio=75) # aqui se crea el objeto articulo pero no se inserta en la tabla
    elem2.save()                                                     # con esta funcion se inserta el articulo en la tabla.
    
    