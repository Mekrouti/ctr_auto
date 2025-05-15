from django.shortcuts import render
from cars.models import *  # ou ton modèle réel s'il a un autre nom
from .models import *  # ou ton modèle réel s'il a un autre nom

# Create your views here.
from django.http import HttpResponse


def home(request):
    cars = Cars.objects.all()

    year = request.GET.get('year')
    marque_id = request.GET.get('marque')
    model = request.GET.get('model')
    category_id = request.GET.get('category')
    boite = request.GET.get('boite')
    origine = request.GET.get('origine')

    if year:
        cars = cars.filter(year=year)
    if marque_id:
        cars = cars.filter(marque_id=marque_id)
    if model:
        cars = cars.filter(model__icontains=model)
    if category_id:
        cars = cars.filter(category_id=category_id)
    if boite:
        cars = cars.filter(Boite_de_vitesses=boite)
    if origine:
        cars = cars.filter(Origine=origine)

    # données pour le formulaire
    years = Cars.objects.values_list('year', flat=True).distinct().order_by('-year')
    marques = Marques.objects.all()
    models = Cars.objects.values_list('model', flat=True).distinct().order_by('model')
    categories = Category.objects.all()
    boites = Cars.objects.values_list('Boite_de_vitesses', flat=True).distinct()
    origines = Cars.objects.values_list('Origine', flat=True).distinct()

    context = {
        'cars': cars,
        'years': years,
        'marques': marques,
        'models': models,
        'categories': categories,
        'boites': boites,
        'origines': origines,
    }

    
    return render(request, 'index.html', context)  # s’il est dans core/templates/home.html



from .models import Accessoire


def accessoire_view(request):
    accessoires = Accessoire.objects.all()

    context = {
        'accessoires': accessoires
    }
    return render(request, 'accessoire/accessoire.html', context)




def accessoire_detail(request):

    return render(request, 'accessoire/access_detail.html', )




