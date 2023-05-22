from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path("", views.welcome_page),


    path("about/", views.about)
]
