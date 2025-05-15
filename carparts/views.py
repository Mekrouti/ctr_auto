

from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404
from .models import *  # ou ton modèle réel s'il a un autre nom




from .forms import *


# Create your views here.

# views.py
from django.shortcuts import render
from .models import Vehicle, Category_auto_parts
from .forms import VehicleMultiFilterForm


 



def catalogue_view(request):
    vehicle_id = request.GET.get('vehicle_id')
    vehicles = Vehicle.objects.all()
    form = VehicleMultiFilterForm(request.GET or None)
    vehicles = Vehicle.objects.all()

    if form.is_valid():
        if form.cleaned_data['marque']:
            vehicles = vehicles.filter(marque__icontains=form.cleaned_data['marque'])
        if form.cleaned_data['model_name']:
            vehicles = vehicles.filter(model_name__icontains=form.cleaned_data['model_name'])
        if form.cleaned_data['engine']:
            vehicles = vehicles.filter(engine__icontains=form.cleaned_data['engine'])
        if form.cleaned_data['year']:
            vehicles = vehicles.filter(year__icontains=form.cleaned_data['year'])

    categories = Category_auto_parts.objects.prefetch_related('subcategories').all()

    return render(request, 'car_part/catalog_parts.html', {
        'vehicles': vehicles,
        'categories': categories,
        'form': form,

    })


