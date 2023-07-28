"""it_sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# CALLING URL NAME AND THE FUNCTION IN views.py

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index1,name='index'),

    path('register1',views.register1,name='register1'),
    path('login1',views.login1,name='login1'),
    path('home1',views.home1,name='home1'),
    path('logout1',views.logout1,name='logout1'),
    path('request', views.request, name='request'),
    path('down', views.down, name='down'),

    path('reqkey', views.reqkey, name='reqkey'),




]

urlpatterns += staticfiles_urlpatterns()
