from django.db import models
from shortner.utils import generate_code,create_shortcode

class ShortURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_ = super(ShortURLManager,self).all(*args,**kwargs)
        qs = qs_.filter(active = True )
        return qs

    def refresh_shortcode(self):    
        qs = Short.objects.filter(id__gte = 1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print( q.shortcode)
            q.save()
            new_codes +=1
        return "new codes made {i}".format(i = new_codes)         

class Short(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,unique=True,default="mgk@",blank = True)
    update = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add= True)
    active = models.BooleanField(default=True)

    objects = ShortURLManager()
    def save(self, *args,**kwargs):
        print('something')
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(Short,self).save( *args,**kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)    
    