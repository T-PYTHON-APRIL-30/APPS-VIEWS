from django.urls import path
from . import views

appName = 'shop'

urlpatterns = [
    path('',views.homePage, name='home'),
    path("about/", views.aboutPage, name="about")
]
