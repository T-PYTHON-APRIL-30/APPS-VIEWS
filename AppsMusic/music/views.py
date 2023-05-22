from django.shortcuts import render
from django.http import HttpRequest, HttpResponse




# Create your views here.
def welcome_page(request):
    return HttpResponse ("Hello World, This is my new HOME")

def about(request):
    return HttpResponse ("this about us page")
