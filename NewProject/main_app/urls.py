from . import views
from django.urls import path

app_name="main_app"

urlpatterns = [
    path("",views.homepage,name="home page"),
    path("about/",views.aboutpage,name="about us")
    
]
