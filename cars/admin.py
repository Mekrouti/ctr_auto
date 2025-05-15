
# Register your models here.
from django.contrib import admin
from .models import Cars, Marques, Category

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('marque', 'model', 'year', 'price', 'km', 'status', 'is_approved')
    list_filter = ('marque', 'status', 'Boite_de_vitesses', 'Origine')
    search_fields = ('model', 'marque__name')
    list_editable = ('is_approved',)

admin.site.register(Marques)
admin.site.register(Category)