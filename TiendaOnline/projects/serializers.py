from rest_framework import serializers
from projects.models import Project , Album,Track
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id","title","description","technology","created_at")
        read_only_fields = ("created_at",)
        
class ProjectSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title","description","technology")
        
# class ProjSeria(serializers.ModelSerializer):
#     datel = serializers.DateTimeField(default_timezone=True)
    
#     class Meta:
#         model = Project
#         fields = ("title","description","datel")

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']
        
class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']