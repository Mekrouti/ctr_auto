from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.

app_name = 'outillage'

def outillage(request):
    categories = Category.objects.all()
    return render(request, 'outillage/outillage.html', {'categories': categories})



def produits_par_categorie(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    produits = Product.objects.filter(category=category)
    return render(request, 'outillage/materiel.html', {
        'category': category,
        'produits': produits
    })





def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'outillage/detail_outil.html', {'product': product})