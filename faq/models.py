from django.db import models

# Create your models here.
class Faq(models.Model):
    faq_title = models.CharField(max_length=250)
    faq_answer = models.TextField(max_length=500)