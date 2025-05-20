from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from users.models import UserRegistrationModel

def custom_admin(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username=usrid, password=pswd)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid admin credentials')

    return render(request, 'custom_admin.html')


def admin_dashboard(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('custom_admin')
    return render(request, 'admin_dashboard.html')


def view_registered_users(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('custom_admin')
    data = UserRegistrationModel.objects.all()
    return render(request, 'user_list.html', {'users': data})


def admin_activate_users(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('custom_admin')

    user_id = request.GET.get('uid')
    if user_id:
        UserRegistrationModel.objects.filter(id=user_id).update(status='activated')
        messages.success(request, 'User activated successfully')
    return redirect('view_registered_users')
