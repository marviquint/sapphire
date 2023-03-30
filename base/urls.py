from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('otp/', views.otp, name='otp'),
    #path('sample/', views.sample, name='sample'),
    path('home/', views.home, name='home'),
    path('url/', views.url, name='url'),
    path('search/', views.search, name='search'),
    path('adduser/', views.addUser, name='addUser'),
]
