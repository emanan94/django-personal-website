from django.shortcuts import render
from .models import Service,Facts
from django.views.generic import ListView

# Create your views here.

class ServiceList(ListView):
    model= Service