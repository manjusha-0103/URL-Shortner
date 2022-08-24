from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

def short_view(request,*args,**kwargs): #function base view fbv
    return HttpResponse("Hello from fbv")

class ShortCBview(View): # class base view cbv  
    def get(request,*args,**kwargs) :
        return  HttpResponse("Hello from CBV ")
