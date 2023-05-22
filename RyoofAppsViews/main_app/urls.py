from django.urls import path
from . import views

app_name="main.app"

urlpatterns=[

    path("",views.home_page,name="Home_page"),
    path("about/",views.overview,name="overview")
]