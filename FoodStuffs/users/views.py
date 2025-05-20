from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from users.models import UserRegistrationModel


User = get_user_model()

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        mobile = request.POST['mobile']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'register.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "User registered successfully.")
        return redirect('login_user')

    return render(request, 'register.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate checks against database
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('main')  # use the correct name of your dashboard route
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request,'login.html')  # send back to login if auth fails

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def main_page(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    return render(request, 'main.html')


def learnmore(request):
    return render(request, 'learn-more.html')


def personalhy(request):
    return render(request, 'personalhy.html')


def food(request):
    return render(request, 'food.html')


def drinks(request):
    return render(request, 'drinks.html')


def health(request):
    return render(request, 'health&wellness.html')
