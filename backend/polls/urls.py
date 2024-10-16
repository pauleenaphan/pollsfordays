from django.urls import path
from . import views
from .views import TestModelListCreate, TestModelDetail # imports view classes we defined

# Routing list that django uses to match incoming request
urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL of the app to the index view
    path('testmodels/', TestModelListCreate.as_view(), name='testmodel-list-create'),
    path('testmodels/<int:pk>/', TestModelDetail.as_view(), name='testmodel-detail')
]