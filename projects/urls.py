from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from . views import ProjectViewset, ProjectOnlyViewSet, ProjectByIdViewSet

router = routers.DefaultRouter()
router.register(r'users', ProjectViewset, basename='project')

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls)),
    path('project_only/', ProjectOnlyViewSet.as_view(), name="project_only"),
    path('project_by_id/<int:id>', ProjectByIdViewSet.as_view(), name="project_by_id"),

    
]