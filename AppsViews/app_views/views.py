from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home_page(request:HttpRequest):

    return HttpResponse("Hello World, This is my new HOME !")


def about(request:HttpRequest):
    #content= 
    return HttpResponse('this website will be the start of my carrer as a \
                        great full stack developer.')
