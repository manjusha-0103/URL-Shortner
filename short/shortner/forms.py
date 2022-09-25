from turtle import textinput
#from typing_extensions import Required
from django import forms
from .validate import validate_url

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label = "URL ",validators = [validate_url],
                        widget=forms.TextInput(
                            attrs= { 
                                    "placeholder" : "Enter URL ",
                                    "class" :"form-control",
                                }
                            )
                        )

    ''' 
    def clean(self):
        clean_data = super(SubmitUrlForm,self).clean()
        url = clean_data.get("url")
        print(url)'''

    '''
    def clean_url(self):    
        url = self.clean_data['url']
        print(url)
        return url'''
