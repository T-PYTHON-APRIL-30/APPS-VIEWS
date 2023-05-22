from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.


def welcome_home_page(request:HttpRequest):
    return HttpResponse ("Hello World, This is my new HOME !")

def about_website(request:HttpRequest):
    return HttpResponse ("Movie browsing website")