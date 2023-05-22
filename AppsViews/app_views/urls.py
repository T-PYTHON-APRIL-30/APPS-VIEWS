from django.urls import path
from . import views

app_name = "app_views"

urlpatterns = [
    path('',views.home_page, name='homepage'),
    path('about/',views.about, name='about')
]