from django.db import models

# Create your models here.
class about(models.Model):
    about_us = models.TextField(max_length=500, blank=False)  
    note = models.TextField(max_length=500, blank=True)
    
    
class service(models.Model):   
    service_name = models.CharField(max_length=50, null=True)
    service_avatar = models.ImageField(upload_to='photos/services', null=True)
    
    
    def __str__(self):
        return self.service_name
    
    
    
    
class testimony(models.Model):
    testimony_name = models.CharField(max_length=50)
    testimonies_avatar = models.ImageField(upload_to='photos/testimonies', blank=True)
    testimony_body = models.TextField(max_length=500, blank=True)
    university = models.CharField(max_length=250, blank=True)
    
    
    def __str__(self):
        return self.testimony_name
    
    
    
    class Meta:
        verbose_name = ('testimony')
        verbose_name_plural = ('testimonies')