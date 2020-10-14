from django.shortcuts import render
from .models import Service,Facts
from django.views.generic import ListView

# Create your views here.

class ServiceList(ListView):
    model= Service
   # extra_context=Facts.objects.last() # listview attribute to get another data  from another model in same view #  last() cuze its one DB wich doesnt need creating a new one just edit on it
    #or
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["x"] = Facts.objects.last() #query
        return context
    