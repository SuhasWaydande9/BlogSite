from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from CreateBlog.models import Blog

# Create your views here.
def MainPage(request):
    Blogs = Blog.objects.all()
    username = request.user.username
    return render(request,template_name='MainPage/home.html',context={'Blogs':Blogs,'username' : username})

def BlogPage(request, id):
    blog = Blog.objects.get(id=id)
    username = request.user.username
    return render(request,template_name='BlogPage/blog.html', context={'Blog':blog, 'username' : username})

def BlogCategory(request, cat):
    blogs = Blog.objects.filter(category = cat)
    username = request.user.username
    return render(request,template_name='MainPage/home.html', context={'Blogs':blogs, 'username' : username})
