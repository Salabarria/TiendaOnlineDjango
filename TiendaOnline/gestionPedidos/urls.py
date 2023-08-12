from django.urls import path
from gestionPedidos.views import GestionPedidosViews


urlpatterns = [
    path('gp/', GestionPedidosViews.as_view(),name="GPV"),
    path('gp/<int:id>', GestionPedidosViews.as_view(),name="articulos methodos PUT y DELETE"),
    
]
