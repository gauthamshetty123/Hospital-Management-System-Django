"""
URL configuration for Hospital project.

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

from .import views 
from .views import add_appointment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name ='base'),

    path('patient/',views.ADD_PATIENT,name='add_patient'),
    path('patients/', views.ALL_PATIENTS, name='all_patients'), 
    path('patient1/', views.ABOUT_PATIENT, name='about_patient'), 
    path('patient2/', views.EDIT_PATIENT, name='edit_patient'), 
    path('add_doctor/', views.ADD_DOCTOR, name='add_doctor'),
    path('all_doctor/', views.all_doctors, name='all_doctors'),
    path('doctor1/', views.ABOUT_DOCTOR, name='about_doctor'),
    path('doctor2/', views.EDIT_DOCTOR, name='edit_doctor'),
    path('appoint1/',views.add_appointment, name='add_appointment'),
    path('appointment/', views.all_appointment, name='all_appointment'),  

]


