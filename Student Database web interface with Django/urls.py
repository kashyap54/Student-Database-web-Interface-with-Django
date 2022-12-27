"""assignment4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.showstu, name = "showstu"),
    path('Insert', views.Insertemp, name = "Insertemp"),
    path('Insert2',views.Insertcor, name = "Insertcor" ),
    path('Edit/<int:id>', views.Editstu, name="Editstu"),
    path('Update/<int:id>', views.Updatestu, name = "Updatestu"),
    path('Edit2/<int:id>', views.Editcor, name="Editcor"),
    path('Update2/<int:id>', views.Updatecor, name = "Updatecor"),
    path('Delete/<int:id>',views.Deletestu, name="Deletestu"),
    path('Delete2/<int:id>',views.Deletecor, name="Deletecor"),
]
