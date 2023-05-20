from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),  # a path for route of homepage
]
