from django.db import models
from shortner.utils import generate_code,create_shortcode
from short import settings

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShortURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_ = super(ShortURLManager,self).all(*args,**kwargs)
        qs = qs_.filter(active = False )
        return qs

    def refresh_shortcode(self, items= None): 
        print(items[0])  
        #print(id) 
        qs = Short.objects.filter(id__gte = 1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')

        new_codes = 0
        print(qs)
        for q in qs:
            q.shortcode = create_shortcode(q)
            print( q.id)
            q.save()
            new_codes += 1
        return "new codes made {i}".format(i = new_codes)         

class Short(models.Model):
    #id_auto = models.AutoField(primary_key=True)
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=SHORTCODE_MAX,unique=True,default="mgk@",blank = True)
    update = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add= True)
    active = models.BooleanField(default=True)

    objects = ShortURLManager()
    def save(self, *args,**kwargs):
        #print('something')
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(Short,self).save( *args,**kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)    
    
    '''class Meta:
        ordering = '-id' '''