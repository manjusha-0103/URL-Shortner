from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .models import Short
# Create your views here.
def test_view(requestcd):
    return HttpResponse("some shorts")

def short_view(request,shortcode = None,*args,**kwargs): 
    obj = Short.objects.get(shortcode = shortcode) 
    print(request.method)
    print(shortcode)
    #obj = get_object_or_404(Short,shortcode = shortcode)                  #function base view fbv
    return HttpResponseRedirect(obj.url)

class ShortCBview(View):                                # class base view cbv  
    def get(self,request,shortcode = None,*args,**kwargs) :
        print(request.method)
        print(shortcode)
        #obj = get_object_or_404(Short,shortcode = shortcode) 
        
        obj = Short.objects.get(shortcode = shortcode) 
        return HttpResponseRedirect(obj.url)

    def get(self,request,shortcode = None,*args,**kwargs) :
        return HttpResponse()
