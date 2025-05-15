from django.contrib import admin

# Register your models here.
from .models import Vehicle, Category_auto_parts, SubCategory_auto_parts

# Enregistrement simple
admin.site.register(Vehicle)
admin.site.register(Category_auto_parts)
admin.site.register(SubCategory_auto_parts)