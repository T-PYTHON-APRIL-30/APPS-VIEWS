from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def homepage(request: HttpRequest):



    return HttpResponse("Hello World, This is my new HOME !")

def aboutpage(request: HttpRequest):


    return HttpResponse('Our web site capable to scraper any site to you want!!')