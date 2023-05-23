from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('about/', views.about, name = 'about'),
    path('home/', views.home, name = 'home')
]
