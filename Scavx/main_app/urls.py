from django.urls import path
from . import views

app_mane="main_app"

urlpatterns=[
    path("",views.home_page,name="home_page"),
    path("about/",views.about_page,name="ab")
]