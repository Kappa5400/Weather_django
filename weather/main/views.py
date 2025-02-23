from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def city(request):
    return render(request,"city.html")

def data(request):
    return render(request, "data.html")

# Create your views here.
