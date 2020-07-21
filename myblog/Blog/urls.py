from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage, name='index'),
    path('category/<str:cat>', views.BlogCategory, name='index'),
    path('Blog/<int:id>', views.BlogPage, name='MainPage')
]