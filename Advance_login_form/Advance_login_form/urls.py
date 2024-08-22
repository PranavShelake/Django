"""
URL configuration for Advance_login_form project.

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
from django.contrib import admin
from django.urls import path
from account.views import login_page, register, reset_password, verification,logout_page,verify_email
from home.views import success
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('register/', register, name='register'),
    path('verify_email/', verify_email, name='verify_email'),
    path('reset_password/<id>/', reset_password, name='reset_password'),
    path('', login_required(success, login_url='login_page'), name='success'),    
    path('verification/', verification, name='verification'),
    path('admin/', admin.site.urls),
]