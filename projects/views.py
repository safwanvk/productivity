from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

from datetime import datetime, timedelta
from .models import Project

# Employee Viewset
from .serializer import ProjectSerializer


class ProjectViewset(viewsets.ViewSet):

    def create(self, request):
        try:
            serializer = ProjectSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"error": False, "message": "Project Data Save Successfully"})
        except:
            return Response({"error": True, "message": "Error During Saving Project Data"})


    def list(self, request):
        try:
            project = Project.objects.all()
            serializer = ProjectSerializer(project, many=True, context={"request": request})
            return Response({"error": False, "message": "All Project List Data", "data": serializer.data})

        except:
            return Response({"error": True, "message": "Error During Project List Data"})


    def retrieve(self, request, pk=None):
        try:
            queryset = Project.objects.all()
            project = get_object_or_404(queryset, pk=pk)
            serializer = ProjectSerializer(project, context={"request": request})
            return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})
        
        except:
            return Response({"error": True, "message": "Error During Project Single Data Fetch"})

    def update(self, request, pk=None):
        try:
            queryset = Project.objects.all()
            project = get_object_or_404(queryset, pk=pk)
            serializer = ProjectSerializer(project, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            return Response({"error": False, "message": "Data Has Been Updated"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Updated"})

    def destroy(self, request, pk=None):
        try:
            queryset = Project.objects.all()
            project = get_object_or_404(queryset, pk=pk)
            project.delete()
            return Response({"error": False, "message": "Data Has Been Deleted"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Deleted"})

class ProjectOnlyUserViewSet(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.kwargs["user_id"]
        return Project.objects.filter(user=user)

class ProjectByIdUserViewSet(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        id = self.kwargs["project_id"]
        user = self.kwargs["user_id"]
        return Project.objects.filter(id=id, user=user)

