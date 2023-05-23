from django.urls import path
from . import views

app_name = "firsta_app"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about/", views.aboutpage, name="aboutpage")
]