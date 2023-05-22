from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def homePage(request:HttpRequest):
    return HttpResponse('Hello World, This is my new HOME !')

def aboutPage(request:HttpRequest):
    return HttpResponse('A simple paragraph about the website.')