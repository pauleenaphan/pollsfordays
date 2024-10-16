from rest_framework import serializers
from .models import TestModel # import our model

# Serializers: 
# Used to convert complex data types into native python data types
# Handles incoming data and validates it
# You need a serializer for each model

class TestModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)  # Include the id field

    class Meta:
        model = TestModel  # Your actual model class
        fields = ['id', 'name']  # Include 'id' in the fields list

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = str(instance.id)  # Convert the id field to string if necessary
        return rep