from django.shortcuts import render
from django.core.mail import send_mail
from accounts.models import account
from about.models import testimony



def home(request):
    testimonies = testimony.objects.all()
    context = {'testimonies': testimonies}
    return render(request, 'home.html', context)



def contact(request):    
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        phone_number = request.POST['phone-number']
        message = request.POST['message']
        
        #Sending an email
        send_mail(
            "message_name",
            "message_email"
            "message",
            "example@email.com",
            ["michaelfeelings@gmail.com", "michaelfeelings@gmail.com"],
        )
        
        return render(request, 'contact.html', {'message_name':message_name})
    else:
        return render(request, 'contact.html', {})
    
    
def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')
