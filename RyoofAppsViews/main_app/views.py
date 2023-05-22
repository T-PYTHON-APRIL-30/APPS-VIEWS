from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_page(request:HttpResponse):

    return HttpResponse("Hello World, This is my new HOME !")

def overview(request:HttpResponse):
    
    return HttpResponse("A simple paragraph about the website.")