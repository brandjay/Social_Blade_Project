from django.shortcuts import render

# Create your views here.
# this page is where the login page sends you. 
# Create a bio with a picture you can change 
# all your uploads/post 

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from matplotlib.style import context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def profile(request):

    return render(request, 'profile.html' )

