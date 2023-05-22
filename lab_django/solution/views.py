from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request:HttpResponse):
    return HttpResponse("Hello World, This is my new HOME !")

def about_page(request:HttpResponse):
    return HttpResponse("Hello this is the about of the page: this app is for the lab view,apps django framework part of python bootcamp")

