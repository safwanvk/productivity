from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

from datetime import datetime, timedelta
from .models import List, ListItem

# Employee Viewset
from .serializer import ListSerializer, ListItemSerializer


class ListViewset(viewsets.ViewSet):

    def create(self, request):
        try:
            serializer = ListSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"error": False, "message": "List Data Save Successfully"})
        except:
            return Response({"error": True, "message": "Error During Saving List Data"})


    def list(self, request):
        try:
            list = List.objects.all()
            serializer = ListSerializer(list, many=True, context={"request": request})
            return Response({"error": False, "message": "All List List Data", "data": serializer.data})

        except:
            return Response({"error": True, "message": "Error During List Data"})


    def retrieve(self, request, pk=None):
        try:
            queryset = List.objects.all()
            list = get_object_or_404(queryset, pk=pk)
            serializer = ListSerializer(list, context={"request": request})
            return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})
        
        except:
            return Response({"error": True, "message": "Error During List Single Data Fetch"})

    def update(self, request, pk=None):
        try:
            queryset = List.objects.all()
            list = get_object_or_404(queryset, pk=pk)
            serializer = ListSerializer(list, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            return Response({"error": False, "message": "Data Has Been Updated"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Updated"})

    def destroy(self, request, pk=None):
        try:
            queryset = List.objects.all()
            list = get_object_or_404(queryset, pk=pk)
            list.delete()
            return Response({"error": False, "message": "Data Has Been Deleted"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Deleted"})

class ListOnlyUserViewSet(generics.ListAPIView):
    serializer_class = ListSerializer

    def get_queryset(self):
        user = self.kwargs["user_id"]
        return List.objects.filter(user=user)

class ListByIdUserViewSet(generics.ListAPIView):
    serializer_class = ListSerializer

    def get_queryset(self):
        id = self.kwargs["list_id"]
        user = self.kwargs["user_id"]
        return List.objects.filter(id=id, user=user)


class ListItemViewset(viewsets.ViewSet):

    def create(self, request):
        try:
            serializer = ListItemSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"error": False, "message": "List Item Data Save Successfully"})
        except:
            return Response({"error": True, "message": "Error During Saving List Item Data"})
            

    def update(self, request, pk=None):
        try:
            queryset = ListItem.objects.all()
            list_item = get_object_or_404(queryset, pk=pk)
            serializer = ListItemSerializer(list_item, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            return Response({"error": False, "message": "Data Has Been Updated"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Updated"})

    def destroy(self, request, pk=None):
        try:
            queryset = ListItem.objects.all()
            list_item = get_object_or_404(queryset, pk=pk)
            list_item.delete()
            return Response({"error": False, "message": "Data Has Been Deleted"})
        
        except:
            return Response({"error": True, "message": "Error During Data Has Been Deleted"})
