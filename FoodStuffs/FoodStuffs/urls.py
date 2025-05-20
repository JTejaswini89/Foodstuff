"""
URL configuration for FoodStuffs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from users import views
from custom_admin import views as vi

urlpatterns = [
    # Admin URLs
    path('custom_admin/', vi.custom_admin, name='custom_admin'),
    path('admin/dashboard/', vi.admin_dashboard, name='admin_dashboard'),
    path('admin/users/', vi.view_registered_users, name='view_registered_users'),
    path('admin/activate_user/', vi.admin_activate_users, name='admin_activate_users'),
    path('view_registered_users/',vi.view_registered_users,name='view_registered_users'),
    # User URLs
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('main/', views.main_page, name='main'),
    path('learnmore/', views.learnmore, name='learnmore'),
    path('personalhy/', views.personalhy, name='personalhy'),
    path('food/', views.food, name='food'),
    path('drinks/', views.drinks, name='drinks'),
    path('health/', views.health, name='health'),
]

