from rest_framework import serializers
from projects.models import Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id","title","description","technology","created_at")
        read_only_fields = ("created_at",)
        
class ProjectSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title","description","technology")
        
class ProjSeria(serializers.ModelSerializer):
    datel = serializers.DateTimeField(default_timezone=True)
    
    class Meta:
        model = Project
        fields = ("title","description","datel")