from django.contrib import admin
from outillage.models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("titre", "category", )  # Colonnes visibles
    list_filter = ("category",)  # Ajoute un filtre par catégorie
    search_fields = ("titre", "category")  # Champ de recherche

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url")  # Colonnes visibles
    search_fields = ("name",)

