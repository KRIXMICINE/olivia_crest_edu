from django.db import models
from django.urls import reverse
from accounts.models import account

# Create your models here.

class Team(account):
    
    class Meta:
        proxy = True
        
    def get_url(self):
        return reverse('team_single', args=[self.slug])
        
    def __str__(self):
        return self.username
    