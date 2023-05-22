from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_page(request:HttpRequest):

    return(HttpResponse("Hello World, This is my new HOME !"))


def about(request:HttpRequest):

    about_content="A simple paragraph about the website"
    return(HttpResponse(about_content))
