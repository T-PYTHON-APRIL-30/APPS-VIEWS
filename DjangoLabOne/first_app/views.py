from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.

def home_page(request: HttpRequest):
    massege = "Hello World, This is my new HOME !"
    return HttpResponse(massege)

def about_us(request: HttpRequest):
    massege = "You have to solve your labs!"
    return HttpResponse(massege)