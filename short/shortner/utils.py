import random 
import string

from django.conf import Settings

from short import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def generate_code(size = SHORTCODE_MIN,char= string.ascii_lowercase+string.digits):
    return ''.join(random.choice(char) for _  in range(size))

def create_shortcode(instance,size = SHORTCODE_MIN ):
    newcode = generate_code(size = size)
    '''print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)'''
    klass = instance.__class__
    qs = klass.objects.filter(shortcode = newcode ).exists()
    if qs :
        return create_shortcode(size = size)
    return newcode    

