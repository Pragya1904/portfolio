from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def portfolio_index(request):
    if request.method == 'POST':
        contact_name=request.POST['contactName']
        contact_message=request.POST['contactMessage']
        contact_email=request.POST['contactEmail']
        contact_subject=request.POST['contactSubject']

        #send an email
        send_mail(
        contact_subject + " by " + contact_name, # subject
        "Sender Email: "+ contact_email + " \nmessage: "+ contact_message ,# message
        contact_email ,# from email
        ['pragya04r@gmail.com'] , #to email
        )
        return render(request,'index.html')
    else:
        return render(request,'index.html')
