from django.http import HttpResponseRedirect
from django.conf import settings

DEFAULT_URL = getattr(settings,"DEFAULT_ULR_REDIRECT","http://www.shortener.com:8000")

def wildcardRedirect(request,path = None):
    new_url = DEFAULT_URL
    if path is not None:
        new_url = DEFAULT_URL + "/"+path
    return  HttpResponseRedirect(new_url)   
