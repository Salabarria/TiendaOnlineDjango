from django.http import  HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
class GuiView(View):
    def get(self,request):
        return HttpResponse("get de GuiView")
    
    def post(self,request):
        return HttpResponse("post de GuiView")

from projects.serializers import ProjectSerializer
from projects.models import Project
from rest_framework import viewsets


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


