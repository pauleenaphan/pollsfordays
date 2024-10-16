from django.db import models

class TestModel(models.Model):
    # Define other fields as needed
    name = models.CharField(max_length=100)

    class Meta:
        # This makes Django recognize that this is a MongoDB model
        app_label = 'polls'