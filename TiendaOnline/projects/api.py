from projects.models import Project,Album,Track
from rest_framework import viewsets,permissions
from projects.serializers import ProjectSerializer,AlbumSerializer,TrackSerializer
from rest_framework.response import Response

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = ProjectSerializer
    
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

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer   