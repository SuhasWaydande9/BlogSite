from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def Login(request):
    context = {
        'username':request.user.username
    }
    return render(request,'Auth/Login.html', context)

def loginto(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Username Or Password not Correct, Please Try Again")
            return redirect('/auth/Login')


def Signup(request):
    context = {
        'username':request.user.username
    }
    return render(request,'Auth/Signup.html', context)

def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        user = User.objects.create_user(username, email, password)

        return redirect('/auth/Login')

def Logout(request):
    logout(request)
    return redirect('/')

