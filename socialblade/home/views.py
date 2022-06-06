from django import views
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from matplotlib.style import context
from matplotlib.style import context
from django.views.generic import *


# Create your views here.
def index(request):
   
    return render(request, 'index.html')
