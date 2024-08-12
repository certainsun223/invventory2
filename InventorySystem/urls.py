"""
URL configuration for InventorySystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginRegister , name='LoginRegister'),
    path('login/', views.Login , name='Login'),
    path('aser/', views.User , name='User'),
    path('adminuser/', views.AdminUser , name='AdminUser'),
    path('user_delete/', views.delete_user , name='delete_user'),
    path('admininv/', views.AdminInventory , name='AdminInventory'),
    path('adminman/', views.AdminManage , name='AdminManage'),
    path('delete_booking/', views.delete_booking , name='delete_booking'),
    path('profile/', views.profile, name='profile'),
    path('adminreport/', views.AdminReport , name='AdminReport'),
    path('Inventory/', views.UserInventory , name='Inventory'),
    path('adminlogout/', auth_views.LogoutView.as_view(template_name='Logreg.html'), name='AdminLogout'),
    path('login/Inventory/', views.UserInventory , name='Inventory'),
    path('login/adminman/', views.AdminManage , name='AdminManage'),
    path('logout/', views.logoutview, name='logout'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('userhp/', views.UserHomepage , name='UserHomepage'),
]

