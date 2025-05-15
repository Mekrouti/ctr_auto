"""
URL configuration for ctr_auto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accessoire.views import home  # ou le nom de ton app principale
from cars.views import *  # ou le nom de ton app principale

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('accessoire/', include('accessoire.urls')),
    path('cars/', include('cars.urls')),
    path('carparts/', include('carparts.urls')),
    path('carrosserie/', include('carrosserie.urls')),
    path('outillage/', include('outillage.urls')),

    

    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  