from django.shortcuts import render
from accounts.models import account
from . models import about,testimony,service

# Create your views here.
def About(request):
    Services = about.objects.all()
    testimonies = testimony.objects.all()
    services = service.objects.all()
    context = {'Services':Services, 'testimonies':testimonies, 'services':services}    
    return render(request, 'about_us.html', context)

