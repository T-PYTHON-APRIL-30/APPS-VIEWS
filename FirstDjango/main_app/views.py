from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home_page(request: HttpRequest):
    return HttpResponse("Hello World, This is my new HOME !")


def about(request: HttpRequest):
    return HttpResponse("This websit about the Django fremwork lab.")


def home(request: HttpRequest):
    return HttpResponse("Home")
