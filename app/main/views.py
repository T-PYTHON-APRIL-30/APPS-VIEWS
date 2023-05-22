from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_page(request:HttpRequest):
    #handle the page

    return HttpResponse("Hello World, This is my new HOME !")

def about(request:HttpRequest):
    about = "This new project in django"
    return HttpResponse(about)
