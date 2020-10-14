from django.shortcuts import render
from .models import Project,Category
from django.views.generic import ListView
# Create your views here.

class ProjectList(ListView):
    model= Project
