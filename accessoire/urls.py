
from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/accessoires/', views.accessoire_view, name='accessoire_view'),
    path('accessoire_detail/', views.accessoire_detail, name='access_detail'),

]
