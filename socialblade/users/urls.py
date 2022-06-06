from django.urls import path
from django import urls
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
     path('login/', LoginView, {'template_name': 'users/login.html'}, name = 'login'),
     url('signup/',views.signup, name = 'signup'),
     url('posts/',views.posts, name = 'posts'),
     url('postform/',views.postform, name = 'postform'),


]