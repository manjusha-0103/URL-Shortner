from django import forms
from .validate import validate_url,validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label = "submit url",validators = [validate_url])

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
