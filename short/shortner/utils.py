import random 
import string

def generate_code(size = 6 ,char= string.ascii_lowercase+string.digits):
    return ''.join(random.choice(char)for _  in range(size))

def create_shortcode(instance,size = 6):
    newcode = generate_code(size = size)
    '''print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)'''
    klass = instance.__class__
    qs = klass.objects.filter(shortcode = newcode ).exists()
    if qs :
        return create_shortcode(size = size)
    return newcode    

