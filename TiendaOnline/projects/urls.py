from rest_framework import routers
from projects.api import ProjectViewSet,AlbumViewSet
from django.urls import path,include
from projects.views import AlbumCustomView,TrackCustomView


router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
router2 = routers.DefaultRouter()
router3 = routers.DefaultRouter()

router.register('rest_projects',ProjectViewSet)

router1.register('rest_projects_album',AlbumViewSet)

router2.register('custom_album',AlbumCustomView)

router3.register('custom_track',TrackCustomView)

urlpatterns = [ 
               
                path('', include(router.urls)),
                path('', include(router1.urls)),
                path('', include(router2.urls)),
                path('', include(router3.urls)),
    
              ]
 