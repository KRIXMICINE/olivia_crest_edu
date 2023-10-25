from django.urls import path, include
from . import views


# create your url pattern here.

urlpatterns = [
    path('', views.faqs, name='faq'),
]
