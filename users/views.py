from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

from datetime import datetime, timedelta
from .models import User

# Employee Viewset
from .serializer import UserSerializer


class UserViewset(viewsets.ViewSet):

    def create(self, request):
        try:
            serializer = UserSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"error": False, "message": "User Data Save Successfully"})
        except:
            return Response({"error": True, "message": "Error During Saving User Data"})


    def list(self, request):
        try:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True, context={"request": request})
            return Response({"error": False, "message": "All User List Data", "data": serializer.data})

        except:
            return Response({"error": True, "message": "Error During User List Data"})


    def retrieve(self, request, pk=None):
        try:
            queryset = User.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer = UserSerializer(user, context={"request": request})
            return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})
        
        except:
            return Response({"error": True, "message": "Error During User Single Data Fetch"})

    def update(self, request, pk=None):
        try:
            queryset = User.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer = UserSerializer(user, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            return Response({"error": False, "message": "Data Has Been Updated"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Updated"})
