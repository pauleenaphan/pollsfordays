from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from .models import TestModel, PollModel
from .serializers import TestModelSerializer, PollModelSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("hell this os a poll")

# class inherits from ListCreateAPI a built in drf that lets you list and create objects
# allows you to handle both get and post instances of test model
class TestModelListCreate(generics.ListCreateAPIView):
    queryset = TestModel.objects.all() # specifics teh data that will be used when listing the models
    serializer_class = TestModelSerializer # specifies which serializer to use for incoming data 

    def perform_create(self, serializer):
        # This will automatically call the serializer's create method
        serializer.save()

# used for get, put, and delete 
class TestModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
    
    # Override this method to fetch the object by 'name'
    def get_object(self):
        name = self.kwargs['name']
        return get_object_or_404(TestModel, name=name)
    

class PollModelCreate(generics.ListCreateAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollModelSerializer

    def perform_create(self, serializer):
        serializer.save()

class PollModelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollModelSerializer
    lookup_field = "_id"

    def get_object(self):
        return super().get_object() # Fetches any objects based on URL params
