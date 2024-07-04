from django.urls import path
from .views import index, contacto, empanadas, categorias, pago, guardar_direccion_envio
"""
URL configuration for ecommerce project.

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

urlpatterns = [
    path('', index.index, name='index'),
    path('contacto/', contacto.contacto, name='contacto'),
    path('empanadas/', empanadas.empanadas, name='empanadas'),
    path('categorias/', categorias.categorias, name='categorias'),
    path('pago/', pago.pago, name='pago'),
    path('guardar-direccion-envio/', guardar_direccion_envio.guardar_direccion_envio, name='guardar_direccion_envio'),
]