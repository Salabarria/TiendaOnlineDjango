import json
from typing import Any
from django import http
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest, JsonResponse
from django.views import View
from .models import Articulos
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
def home(request):
    return HttpResponse(" funcion home invocada por url home/")

def gui(request):
    return HttpResponse(" funciion gui invocada por url salida/ ")
def penco(request,id):
    return HttpResponse(" funciion penco invocada por url con paramentros dinamiscos id ")

class GestionPedidosViews(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    
    def metodo1(request,id):
        print(id)
        return HttpResponse("metodo view llamdo metodo1 invocado desde clase definida en views asocoada a una url")
    
    
    def get(self,request,id = 0):
        
        if(id > 0):
            articulos = list(Articulos.objects.filter(id=id).values())
            if len(articulos)>0:
                arti = articulos[0]
                datos = {"message" : "Success","Articulos":arti}
            else:
                datos = {"message" : "articulos not found ... "}
            return JsonResponse(datos)    
                
            
        else:           
             all_articulos = list(Articulos.objects.values())
             if len(all_articulos)>0:
                datos = {"message" : "Success","Articulos":all_articulos}
             else:
                datos = {"message" : "articulos not found ... "}
             return JsonResponse(datos)
        
        # return HttpResponse("metodo get de la la clase GestionPedidos")
    def post(self,request):
        print(request.body)
        jsondata = json.loads(request.body)
        print(jsondata)
        Articulos.objects.create(nombre = jsondata["nombre"],seccion = jsondata["seccion"],precio=jsondata["precio"])
        
        datos = {"message" : "articulos not found ... "}
        
        return JsonResponse(datos)
   
    
    def put(self,request,id):
        jsondata = json.loads(request.body)
        articulo = list(Articulos.objects.filter(id=id).values())
        if len(articulo)>0:
            articulo_id = Articulos.objects.get(id=id)
            articulo_id.nombre = jsondata["nombre"]
            articulo_id.seccion = jsondata["seccion"]
            articulo_id.precio = jsondata["precio"]
            articulo_id.save()
            datos = {"message" : "Success"}          
        else:
            datos = {"message" : "articulos not found ... "}
        return JsonResponse(datos)
    
    
    def delete(self,request,id):
        
        articulos = list(Articulos.objects.filter(id=id).values())
        if len(articulos)>0:
            
            Articulos.objects.filter(id=id).delete()
            datos = {"message" : "Success"}
        else:
            datos = {"message" : "articulos not found ... "}
        return JsonResponse(datos)    
        
        

    