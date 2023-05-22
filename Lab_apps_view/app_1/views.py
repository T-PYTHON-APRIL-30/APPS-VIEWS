from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.

def home_page (request:HttpRequest):

    return HttpResponse("Hello World, This is my new HOME !")

def about (request:HttpRequest):
    content = "Wlcome to my online shopping store\nThe website is established at 2023-5-22"
    return HttpResponse (content)