from django.urls import path
from . import views

urlpatterns = [
    path('outillage/', views.outillage, name='outillage'),
]