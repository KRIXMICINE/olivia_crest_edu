from django.db import models
from accounts.models import account
from taggit.managers import TaggableManager
from category.models import category
from django.urls import reverse
from django.utils import timezone


#Create your models here.

class post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    intro = models.TextField(max_length=500, blank=False)
    post_image = models.ImageField(upload_to='photos/post', blank=True, default=None)
    author = models.ForeignKey(account, on_delete=models.PROTECT, blank=False)
    author_avatar = models.ImageField(upload_to='photos/blog', blank=True, default=None)
    author_bio = models.TextField(max_length=200, blank=False)
    Tags = TaggableManager()
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=None)
    
    
    
    def get_url(self):
        return reverse('blog_details', args=[self.category.slug,self.slug])
    
    
    class Meta:
        ordering = ('publish',)
        
        
    def __str__(self):
        return self.title
    