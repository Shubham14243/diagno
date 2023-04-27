"""diagno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='Index'),
    path('index/', views.home, name='Home'),
    path('login/', views.log, name='Login'),
    path('register/', views.reg, name='Register'),
    path('doctor/', views.doc, name='Doctor'),
    path('doclogin/', views.doclog, name='Doctor Login'),
    path('docregister/', views.docreg, name='Doctor Register'),
    path('admin_login/', views.admlog, name='Admin Login'),
    path('dashuser/', views.udash, name='User Dashboard'),
    path('dashdoc/', views.ddash, name='Doctor Dashboard'),
    path('dashadmin/', views.adash, name='Admin Dashboard'),
    path('result/', views.result, name='Result'),
    path('ureset/', views.ures, name='Reset User Password'),
    path('dreset/', views.dres, name='Reset Doctor Password'),
    path('areset/', views.ares, name='Reset Admin Password'),
    path('reg/', views.register_user, name='User Registration'),
    path('log/', views.login_user, name='User Login'),
    path('logout/', views.logout, name='User Logout'),
    path('diag/', views.diag, name='Diagnose User'),
    path('appt/', views.appt, name='Book Appointment'),
    path('delapp/', views.delapp, name='Delete Appointment'),
    path('updapp/', views.updapp, name='Update Appointment'),
    path('updpro/', views.updpro, name='Update Profile'),
    path('updpass/', views.updpass, name='Update Password'),
    path('delpro/', views.dellpro, name='Delete Profile'),
    path('regdoc/', views.register_doctor, name='Doctor Registration'),
    path('logdoc/', views.login_doctor, name='Doctor Login'),
    path('doclogout/', views.doclogout, name='Doctor Logout'),
    path('upddocpro/', views.upddocpro, name='Update Doctor Profile'),
    path('upddocpass/', views.upddocpass, name='Update Doctor Password'),
    path('deldocpro/', views.delldocpro, name='Delete Doctor Profile'),
    path('adlog/', views.login_admin, name='Admin Login'),
    path('logadmin/', views.login_admin, name='Admin Login'),
    path('admlogout/', views.admlogout, name='Admin Logout'),
    path('updadminpro/', views.updadmpro, name='Update Admin Profile'),
    path('updadminpass/', views.updadpass, name='Update Admin Password'),
    path('deladminpro/', views.delladpro, name='Delete admin Profile'),
    path('approve/', views.approve, name='Approve Appointment'),
    path('cancel/', views.cancel, name='Approve Appointment'),
    path('feedback/', views.get_feed, name='Get Feedback'),
    path('verifyotp/', views.otp_varify, name='Varify OTP'),
    path('ureset/', views.ures, name='Reset User Password'),
    path('resetuser/', views.resetuser, name='Set New User Password'),
    path('dreset/', views.dres, name='Reset Doctor Password'),
    path('resetdoc/', views.resetdoc, name='Set New Doc Password'),
    path('areset/', views.ares, name='Reset Doctor Password'),
    path('resetadm/', views.resetadm, name='Set New Doc Password')
]
