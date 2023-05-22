from django.urls import path
from . import views

app_name = "app_one"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]
