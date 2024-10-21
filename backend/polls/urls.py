from django.urls import path
from . import views
from .views import TestModelListCreate, TestModelDetail, PollModelCreate, PollModelList, PollModelDetails, UserCreate, UserLogin # imports view classes we defined


# Routing list that django uses to match incoming request
urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL of the app to the index view
    path('testmodels/', TestModelListCreate.as_view(), name='testmodel-list-create'),
    path('testmodels/<str:name>/', TestModelDetail.as_view(), name='testmodel-detail'),

    path("pollmodels/create/", PollModelCreate.as_view(), name="pollmodel-create"),
    path("pollmodels/getAllPolls", PollModelList.as_view(), name="pollmode-getall"),
    path("pollmodels/<str:_id>/", PollModelDetails.as_view(), name="pollmodel-details"),

    path("signup/", UserCreate.as_view(), name="user-signup"),
    path("login/", UserLogin.as_view(), name="user-login")
]