from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Hello World, This is my new HOME !")


def about(request):
    return HttpResponse("This websit about the Django fremwork lab.")


def home(request):
    return HttpResponse("Home")
