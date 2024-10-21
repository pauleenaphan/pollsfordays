from djongo import models
from bson import ObjectId # Used to work with mongoID
from django.core.exceptions import ValidationError

class TestModel(models.Model):
    _id = models.ObjectIdField(default=ObjectId, editable=False, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        # This makes Django recognize that this is a MongoDB model
        app_label = 'polls'

class PollModel(models.Model):
    _id = models.ObjectIdField(default=ObjectId, editable=False, primary_key=True)
    title = models.CharField(max_length=500, blank=False)
    choices = models.JSONField()  # list field makes the option and array
    author = models.CharField(max_length=20)
    timeLimit = models.IntegerField()  # Stores a single integer, like minutes or hours
    datePosted = models.CharField(max_length=500, blank=False)  # Stores the date as an integer (like timestamp)

    def clean(self):
        super().clean()
        if len(self.choices) < 2:  # Minimum of 2 choices
            raise ValidationError('There must be at least 2 choices.')
        if len(self.choices) > 6:  # Maximum of 10 choices
            raise ValidationError('There cannot be more than 6 choices.')

    class Meta:
        app_label = "polls"