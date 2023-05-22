from django.urls import path
from . import views


app_name = "main_app"

urlpatterns = [
    path("",views.Home_Page, name = "main_app"),
    path("about/",views.about,name="main_app")
]