from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Login, name='index'),
    path('Login', views.Login, name='LogIn'),
    path('Signup',views.Signup, name='SignUp'),
    path('loginto', views.loginto, name='loginto'),
    path('register', views.register, name='register'),
    path('logout', views.Logout, name='Logout')
]