from django.urls import re_path
from .views import homePage

urlpatterns = [
    path("", homePage, name="home"),
]
