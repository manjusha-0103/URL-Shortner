from itertools import count
from django.db import models

# Create your models here.
from shortner.models import Short


class ClickEventManager(models.Manager):
    def count_clicks(self,shortinstance):
        if isinstance(shortinstance,Short):
            obj, created = self.get_or_create(short_url = shortinstance)
            obj.count += 1
            obj.save()
            return obj.count
        else :
            return None   

class ClickEvent(models.Model):
    short_url   = models.OneToOneField(Short,on_delete=models.CASCADE)
    count       = models.IntegerField(default=0)
    update      = models.DateField(auto_now=True)
    timestamp   = models.DateField(auto_now_add= True)

    objects = ClickEventManager()
    def __str__(self):
        return f"{self.short_url.get_short_url()} : {self.count}"
