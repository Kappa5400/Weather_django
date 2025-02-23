from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home")
    #insert more views here
]