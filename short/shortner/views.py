from ast import FormattedValue
from re import template
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .models import Short
from .forms import SubmitUrlForm
from django.contrib import messages
from django.db import IntegrityError
'''def get_url(request):
    pass
def post_url(request):
    if request.methond == 'POST':
        the_form = SubmitUrlForm(request.POST)
        if the_form.is_valid():
            the_form.save()

    return render()     '''  


class Home_view(View):
    def get(self,request,*args,**kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title" :"submit url",
            "form" : the_form,
        }
        return render(request,"short\home.html",context)

    def post(self,request,*args,**kwargs): 
        print(request.POST)
        
        form = SubmitUrlForm(request.POST) 
         
        print(form)
        context = {
            "title" :"submit url",
            "form" : form,
        } 
        template = "short\home.html"
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data.get("url"))
            new_url = form.cleaned_data.get("url")
            obj ,created  = Short.objects.get_or_create(url = new_url)

            '''try :
                obj ,created  = Short.objects.get_or_create(url = new_url)
            except IntegrityError:
                messages.error(request,"") '''   
            print(created)
            context = {
                "obj" : obj,
                "created" : created,
            }
            if created :
                template = "short\sucess.html"
            else :
                template = "short\exists_already.html"  
        
        return render(request,template,context)

def short_view(request,shortcode = None,*args,**kwargs): 
    #obj = Short.objects.get(shortcode = shortcode) 
    
    print(request.method)
    print(shortcode)
    obj = get_object_or_404(Short,shortcode = shortcode)
    print(obj)                  #function base view fbv
    return HttpResponseRedirect(obj.url)

class ShortCBview(View):                                # class base view cbv  
    def get(self,request,shortcode = None,*args,**kwargs) :
        print(request.method)
        print(shortcode)
        obj = get_object_or_404(Short,shortcode = shortcode) 
        
        #obj = Short.objects.get(shortcode = shortcode) 
        return HttpResponseRedirect(obj.url)

    def post(self,request,shortcode = None,*args,**kwargs) :
        return HttpResponse()
