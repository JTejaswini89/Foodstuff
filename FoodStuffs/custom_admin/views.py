from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def admin_dashboard(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'admin' and password == 'admin':
            return render(request, 'admin_dashboard.html')
        else:
            return render(request, 'custom_admin.html', {'error': 'Invalid credentials'})
    
    return render(request, 'custom_admin.html')  # if GET request

def custom_admin_home(request):
    return render(request, 'custom_admin.html')