from rest_framework import serializers
from .models import TestModel, PollModel # import our model

# Serializers: 
# Used to convert complex data types into native python data types
# Handles incoming data and validates it
# You need a serializer for each model

# Representation:
# Refers to the process of converting complex python objects to data structure

# self: allows method to access attributes of the instance of the class

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
        
    