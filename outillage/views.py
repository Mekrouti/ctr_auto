from django.shortcuts import render
from .models import *

# Create your views here.



def outillage(request):
    categories = Category.objects.all()
    return render(request, 'outillage/outillage.html', {'categories': categories})