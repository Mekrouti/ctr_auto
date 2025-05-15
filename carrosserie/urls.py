
from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/carrosserie/', views.carrosserie, name='carrosserie'),
]
