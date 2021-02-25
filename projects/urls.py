from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from . views import ProjectViewset

router = routers.DefaultRouter()
router.register(r'', ProjectViewset, basename='project')

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls))
    
]