"""
URL configuration for TiendaOnline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from gestionPedidos.views import home,gui,penco,GestionPedidosViews
from tasks import views

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path( "home/", home),
    path("gui/",gui),
    path("penco/<id>",penco),
    path("clase/<id>",GestionPedidosViews.metodo1),
    path("hola", GestionPedidosViews.get),
    path('gp/', include("gestionPedidos.urls")),
    
    #-url for tasks app ------
    path("home1/", views.home,name="home1" ),
    path("signup/", views.signup, name="signup"),
    path("tasks/", views.tasks, name="tasks"),
    path("logout/", views.signout, name="logout"),
    path("signin/", views.signin , name = "signin"),
    path("task/create/", views.create_task,name = "create_task"),
    path("task/<int:task_id>/", views.task_detail,name = "task_detail"),
    
    #-url for projects app rest framework django  ------
    
    path('projects_app/', include("projects.urls")),
    path('docs/',include_docs_urls(title='api documentation'))    
    
    
]
