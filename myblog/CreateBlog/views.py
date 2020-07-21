from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect ,HttpRequest, request
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import models
from .models import Blog
from .forms import Choices
 

# Create your views here.

def CreateBlog(request):
    if request.user.is_authenticated:
        UserBlogs = Blog.objects.filter(user = request.user)
        username = request.user.username
        context = {
            'UserBlogs':UserBlogs,
            'username':username
        }
        context['form'] = Choices() 
        return render(request, 'CreateBlog/CreateBlog.html', context)
    else:
        messages.error(request, "You Have To Log-In to Create Blog")
        return redirect('/auth/Login')

    
def postblog(request):
    if request.user.is_authenticated:
        blog = Blog(title = request.POST['title'], story = request.POST['story'],category = request.POST['category'] , user = request.user)
        blog.save()    
        return redirect('/')
    else:
        return redirect('/auth/Login')

def postupdate(request, id):
    if request.user.is_authenticated:
        IfItIs = Blog.objects.get(id=id)
        if IfItIs:
            IfItIs.story = request.POST['story']
            IfItIs.title = request.POST['title']
            IfItIs.save()
        else:
            blog = Blog(title = request.POST['title'], story = request.POST['story'],category = request.POST['category'] , user = request.user)
            blog.save()    
        
        return redirect('/')
    else:
        return redirect('/auth/Login')


    

    return redirect('/')

def updateblog(request, id):
        if request.user.is_authenticated:
            ThatUser = Blog.objects.filter(user = request.user)
        if ThatUser:
            ThatBlog = Blog.objects.get(id=id)
            username = request.user.username
            context = {
                'ThatBlog':ThatBlog,
                'username':username
            }
            return render(request, 'CreateBlog/UpdateBlog.html', context)

def deleteblog(request, id):
    if request.user.is_authenticated:
        ThatUser = Blog.objects.filter(user = request.user)
        if ThatUser:
            Blog.objects.get(id=id).delete()
            return redirect('/CreateBlog')
        else:
            messages.add_message(request, message.Warning, "Cant Delete Blog Permission Denied....")
            return redirect('/CreateBlog')