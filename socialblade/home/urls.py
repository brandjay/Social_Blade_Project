from django.urls import path
from django import urls
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
     path('', views.index, name='index'),

]