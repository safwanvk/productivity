from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from . views import TaskViewset, TaskOnlyUserViewSet, TaskByIdUserViewSet

router = routers.DefaultRouter()
router.register(r'', TaskViewset, basename='task')

app_name = 'tasks'

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>', TaskOnlyUserViewSet.as_view(), name="task_only_by_user_id"),
    path('<int:project_id>/user/<int:user_id>', TaskByIdUserViewSet.as_view(), name="task_by_id_by_user_id"),

    
]