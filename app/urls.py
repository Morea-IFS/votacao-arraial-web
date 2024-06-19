from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candidates/', views.candidates, name='candidates'),
    path('result/', views.result, name='result'),
]