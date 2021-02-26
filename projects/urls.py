from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from . views import ProjectViewset, ProjectOnlyUserViewSet, ProjectByIdUserViewSet

router = routers.DefaultRouter()
router.register(r'', ProjectViewset, basename='project')

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>', ProjectOnlyUserViewSet.as_view(), name="project_only_by_user_id"),
    path('<int:project_id>/user/<int:user_id>', ProjectByIdUserViewSet.as_view(), name="project_by_id_by_user_id"),

    
]