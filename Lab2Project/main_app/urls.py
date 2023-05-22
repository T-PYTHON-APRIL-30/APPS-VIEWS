from django.urls import path
from . import views




app_name = "main_app"


urlpatterns = [
    path("", views.welcome_home_page, name="welcome_home_page"),
    path("about/", views.about_website, name="about_website")
]