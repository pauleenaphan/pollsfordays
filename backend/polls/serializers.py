from rest_framework import serializers
from django.contrib.auth.models import User # Django builtin user Model
from .models import TestModel, PollModel # import our model

# Serializers: 
# Used to convert complex data types into native python data types
# Handles incoming data and validates it
# You need a serializer for each model

# Representation:
# Refers to the process of converting complex python objects to data structure

# self: allows method to access attributes of the instance of the class
# super(): use method from parent class
# to_representation: takes data and converts it into a format that is sent to user

class TestModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)  # Include the id field

    class Meta:
        model = TestModel  # Your actual model class
        fields = "__all__" 

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = str(instance._id) 
        return rep
    

class PollModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollModel
        fields = "__all__"

    def to_representation(self, instance):
        return super().to_representation(instance)
        

class UserSerializer(serializers.ModelSerializer):
    # password is built in but we want to make it write_only so we create a new one
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    # Data that will be validated by the serializer
    # Create is used to define how to create an instance of User
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),  # Email is optional, so use .get() to avoid KeyError
            password=validated_data["password"]  # Hashes password automatically
        )
        return user