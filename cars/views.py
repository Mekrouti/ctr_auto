
from django.shortcuts import render, redirect
from .forms import CarForm

from django.shortcuts import render, get_object_or_404
from .models import *  # ou ton modèle réel s'il a un autre nom




def automobile(request):
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

    return render(request, 'cars/automobile.html', context)



def car_vendre(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars:automobile')
    else:
        form = CarForm()
    return render(request, 'cars/car_vendre.html', {'form': form})





 # page pour vendre une voiture


def car_detail(request, id):
    car = get_object_or_404(Cars, id=id)
    context = {'car': car}
    return render(request, 'cars/car_detai.html', context)
