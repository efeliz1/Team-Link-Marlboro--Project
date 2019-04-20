from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()


    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            message = f"{contact_name} has sent you a new message ..."
            email_msg = EmailMessage(
                subject='New Enquiry', body=message,
                from_email='tlmarlborough@zoho.com',
                to=['tlmarlborough@zoho.com'],
                headers={'Reply-To': contact_email})  # <<< where you want replies to go
            email_msg.send()
            
    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'tlmarlborough@zoho.com'
EMAIL_HOST_PASSWORD = 'teamlink123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
