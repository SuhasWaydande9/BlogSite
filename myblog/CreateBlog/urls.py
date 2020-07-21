from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateBlog, name='createblog'),
    path('postblog' ,views.postblog, name='postblog'),
    path('postupdate/<int:id>' ,views.postupdate, name='postblog'),
    path('deleteblog/<int:id>',views.deleteblog, name='deleteblog'),
    path('updateblog/<int:id>',views.updateblog, name='updateblog')
]