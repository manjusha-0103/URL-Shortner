
from django.shortcuts import render,redirect
from .forms import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from short.settings import EMAIL_HOST_USER

def contact_view(request):
    '''
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
            'name': form.cleaned_data['name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }		    
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, form , ['manjushakatkhede96@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("main:homepage")
      
    form = Contact()
    return render(request, "short/base/base.html", {'form':form})
    '''

    '''if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        data = {
            'name' : name,
            'email' : email,
            'meassage' : message,
        } 
        message = f"from {data['name']} \n Message : {data['mesaage']}"
        print(data)  
    return render(request,"short\home.html")'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and message and email:
            #subject = email
            message = f"Email : {email} \nfrom : {name}\nmessage : {message}"
            try:
               print(send_mail("URL-Shortener.com", message, "url-Shortner.com", [EMAIL_HOST_USER]))
            except BadHeaderError:
                return HttpResponse(BadHeaderError)
            return redirect('/')
   
            # In reality we'd use a form class
            # to get proper validation errors.
    #else:
    return redirect('/')
    #return render(request,"short/home.html")
    #return HttpResponse('Make sure all fields are entered and valid.')
        
        
        
        
        
        
        
        
