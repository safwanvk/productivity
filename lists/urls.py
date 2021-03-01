from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from . views import ListViewset, ListOnlyUserViewSet, ListByIdUserViewSet

router = routers.DefaultRouter()
router.register(r'', ListViewset, basename='task')

app_name = 'lists'

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>', ListOnlyUserViewSet.as_view(), name="list_only_by_user_id"),
    path('<int:list_id>/user/<int:user_id>', ListByIdUserViewSet.as_view(), name="list_by_id_by_user_id"),

    
]