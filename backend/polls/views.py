from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from .models import TestModel
from .serializers import TestModelSerializer

# Create your views here.
def index(request):
    return HttpResponse("hell this os a poll")

# defines a new class testmodellistcreeate 
# allows you to handle both get and post instances of test model
class TestModelListCreate(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer

    def perform_create(self, serializer):
        # This will automatically call the serializer's create method
        serializer.save()


# used for get, put, and delete 
class TestModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer

