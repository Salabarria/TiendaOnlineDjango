from projects.serializers import ProjectSerializer,AlbumSerializer,TrackSerializer
from projects.models import Project,Album,Track
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AlbumCustomView(viewsets.ViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    def list(self, request, *args, **kwargs):
        return Response("list ")
    def create (self,request):
        return Response("create ")
    
    
    def read(self,request, *args, **kwargs):
        return Response("read ")
    def update(self,request, *args, **kwargs):
        return Response("update ")
    
    def put(self,request, *args, **kwargs):
        return Response("put ")
        
    def delete (self,request, *args, **kwargs):
        return Response("delete ")
    def patch(self,request, *args, **kwargs):
        return Response("patch")
        
        
        
class TrackCustomView(viewsets.ModelViewSet):
        queryset = Track.objects.all()
        serializer_class = TrackSerializer       
    
    


