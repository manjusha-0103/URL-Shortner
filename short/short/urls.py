"""short URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
#from django.conf.urls import url 
from shortner.views import short_view ,Home_view ,URLRedirectview
from contact.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',Home_view.as_view()),
    #path('contact/',),
    re_path(r'^contact/$',contact_view,name = "contact"),
    #re_path(r'^(?P<shortcode>[\w-]+)$',short_view),
    re_path(r'^(?P<shortcode>[\w-]+)/$',URLRedirectview.as_view(),name = "shortcode"),
]
