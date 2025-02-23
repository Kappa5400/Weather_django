from django.shortcuts import render
from django.http import HttpResponse
from .models import cities

def home(request):
    return render(request, "index.html")

def city(request):
    return render(request,"city.html")

def data(request):
    stuff = cities.objects.all
    return render(request, "data.html",{"cities": stuff})

# Create your views here.
