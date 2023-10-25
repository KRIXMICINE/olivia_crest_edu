from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='team'),
    path('team/<int:pk>/', views.team_single, name='team_single'),
]