"""HomeSmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Shome import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login),
    path('loginPro',views.loginPro),
    path('ap',views.adminPanel),
    path('Adduser',views.AddUser),
    path('Adduser1',views.AddUser1),
    path('AddDevice1',views.AddDevice1),
    path('AddDevices',views.AddDevice2),
    path('deviceCon1',views.deviceCon1),
    path('deviceCon',views.deviceCon),
    path('UserDeviceCon',views.UserDeviceCon),
    path('UserDeviceCon1',views.UserDeviceCon1),
    path('UsersList',views.UsersList),
]
