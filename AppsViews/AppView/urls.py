from django.urls import path
from . import views

app_name="AppView"

urlpatterns=[
    path("",views.home_page,name="home_page"),
    path("about/",views.about,name="about")
]