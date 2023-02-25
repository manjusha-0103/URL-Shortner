from .models import ContactForm
from django.forms import ModelForm

class Contact(ModelForm):
    class Meta :
        model = ContactForm
        fields = '__all__'
