from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from . views import UserViewset

router = routers.DefaultRouter()
router.register(r'', UserViewset, basename='user')

app_name = 'users'

urlpatterns = [
    path('user/', include(router.urls)),
    
]
