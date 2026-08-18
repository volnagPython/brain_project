"""
URL configuration for brain_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from parser_app.views import index_page, specs_bs4, specs_sel, specs_plw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_page),
    path('index.html', index_page),
    path('specs_bs4.html',specs_bs4),
    path('specs_plw.html',specs_plw),
    path('specs_sel.html',specs_sel),
]
