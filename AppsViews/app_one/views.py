from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World, This is my new HOME!")

def about(request):
    return HttpResponse("About the website: Using what I have learned, I should Create a new Django project, with 1 app")