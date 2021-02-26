from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

from datetime import datetime, timedelta
from .models import Task

# Employee Viewset
from .serializer import TaskSerializer


class TaskViewset(viewsets.ViewSet):

    def create(self, request):
        try:
            serializer = TaskSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"error": False, "message": "Task Data Save Successfully"})
        except:
            return Response({"error": True, "message": "Error During Saving Task Data"})


    def list(self, request):
        try:
            task = Task.objects.all()
            serializer = TaskSerializer(task, many=True, context={"request": request})
            return Response({"error": False, "message": "All Task List Data", "data": serializer.data})

        except:
            return Response({"error": True, "message": "Error During Task List Data"})


    def retrieve(self, request, pk=None):
        try:
            queryset = Task.objects.all()
            task = get_object_or_404(queryset, pk=pk)
            serializer = TaskSerializer(task, context={"request": request})
            return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})
        
        except:
            return Response({"error": True, "message": "Error During Task Single Data Fetch"})

    def update(self, request, pk=None):
        try:
            queryset = Task.objects.all()
            task = get_object_or_404(queryset, pk=pk)
            serializer = TaskSerializer(task, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            return Response({"error": False, "message": "Data Has Been Updated"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Updated"})

    def destroy(self, request, pk=None):
        try:
            queryset = Task.objects.all()
            task = get_object_or_404(queryset, pk=pk)
            task.delete()
            return Response({"error": False, "message": "Data Has Been Deleted"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Deleted"})

class TaskOnlyUserViewSet(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.kwargs["user_id"]
        return Task.objects.filter(user=user)

class TaskByIdUserViewSet(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        id = self.kwargs["task_id"]
        user = self.kwargs["user_id"]
        return Task.objects.filter(id=id, user=user)