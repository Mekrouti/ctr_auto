from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/', views.catalogue_view, name='catalogue'),
]