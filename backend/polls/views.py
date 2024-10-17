from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.response import Response
from .models import TestModel, PollModel
from .serializers import TestModelSerializer, PollModelSerializer, UserSerializer
from django.shortcuts import get_object_or_404

from bson import ObjectId

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
    # get_object is HOW you get the values of the object
    def get_object(self):
        name = self.kwargs['name']
        return get_object_or_404(TestModel, name=name)
    

# Used to create and view polls
class PollModelCreate(generics.ListCreateAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollModelSerializer

    def perform_create(self, serializer):
        serializer.save()

# Super is a method from the parent class that contains the default for updating an object
# Used to get, update, and delete polls
class PollModelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollModelSerializer
    lookup_field = "_id"

    def get_object(self):
        _id = self.kwargs.get(self.lookup_field)  # Get the _id from URL parameters
        try:
            # Convert the string _id to ObjectId for querying
            return self.queryset.get(_id=ObjectId(_id))
        except (PollModel.DoesNotExist, Exception):
            raise Http404("PollModel not found.")  # Raise 404 if not found

    # asterisks are used to capture extra arugments, if we remove them then only one arg can be passsed in
    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the current instance
        serializer = self.get_serializer(instance, data=request.data, partial=True) # Use serializer to convert our data
        serializer.is_valid(raise_exception=True)  # Checks if the data is valid
        self.perform_update(serializer)  # Save the updated instance

        print("Poll has been updated", request.data)
        return Response(serializer.data)  # Return the updated data
    
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        print("Poll has been removed", request.data)
        return response
    
# Used to create new Users
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer # specifiies that userseralizer will be used

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED) # Returns object and status code