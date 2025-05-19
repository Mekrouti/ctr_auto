from django.urls import path
from . import views
app_name = 'outillage'
urlpatterns = [
    path('outillage/', views.outillage, name='outillage'),
    path('materiel/<int:category_id>/', views.produits_par_categorie, name='materiel'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail')



]