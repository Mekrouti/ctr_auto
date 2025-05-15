       
from django.urls import path
from . import views





app_name = 'cars'

urlpatterns = [    



    path('automobile/', views.automobile, name='automobile'),  # Nom de chemin corrigé

    path('car_vendre/', views.car_vendre, name='car_vendre'),
    path('car_details/<int:id>/', views.car_detail, name='car_detail'),
    ]
