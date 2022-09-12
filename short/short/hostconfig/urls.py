from django.contrib import admin

from django.urls import path,re_path
from .views import wildcardRedirect

urlpatterns = [
    re_path(r'^(?P<path>.*)', wildcardRedirect , name = "wildcard"),
    
]