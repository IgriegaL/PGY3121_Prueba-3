"""p2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path

from . import views
# from p2.views import inicio, seguimiento, donacion, carritoCompra, productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('seguimiento/', views.seguimiento, name="seguimiento"),
    path('donacion/', views.donacion, name="donacion"),
    path('carritoCompra/', views.carritoCompra, name="carritoCompra"),
    path('productos/', views.productos, name="productos"),
    path('tablas/', views.verTablas, name="tablas"),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', inicio),
#     path('seguimiento/', seguimiento),
#     path('donacion/', donacion),
#     path('carritoCompra/', carritoCompra),
#     path('productos/', productos),
# ]


