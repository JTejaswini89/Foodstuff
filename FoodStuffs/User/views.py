from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Registration successful!')
        return redirect('login_user')
    return render(request, 'Register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'Login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

def main_page(request):
    return render(request, 'main.html')


def learnmore(request):
    return render(request, 'learn-more.html')
