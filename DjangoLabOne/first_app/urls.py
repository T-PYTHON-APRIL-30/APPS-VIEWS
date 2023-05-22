from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
    path("home/",views.home_page, name="home_page"),
    path("about/",views.about_us,name="about_us")
]