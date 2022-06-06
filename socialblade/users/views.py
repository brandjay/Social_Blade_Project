from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from requests import post, request
from users.forms import SignUpForm
from matplotlib.style import context
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import Post

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)# was UserCreationForm
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  #profile
    else:
        form = SignUpForm() #was UserCreationForm
    return render(request, 'signup.html', {'form': form})


#displays post from users

def posts(request):
    userpost = Post.objects.all()
    return render(request, 'posts.html', {'userpost': userpost})


from .forms import PostForm
@login_required()
def postform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST, request.FILES) 
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()

            form.errors
            return HttpResponseRedirect('/users/posts/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'postform.html', {'form': form})