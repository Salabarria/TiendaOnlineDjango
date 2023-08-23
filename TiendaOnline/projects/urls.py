from rest_framework import routers
from projects.api import ProjectViewSet,UserViewSet
from django.urls import path,include
from projects.views import GuiView

router = routers.DefaultRouter()

router.register('rest_projects',ProjectViewSet)
# router.register("api/projects",UserViewSet,"projects")
urlpatterns = [
    
    path('', include(router.urls))
    
    ]
    


# #Ò####3♣
# urlpatterns = [
#     path("guillermoview/", GuiView.as_view()),
    
    
# ]
