from django import forms
from .models import Cars

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = [
            'marque', 'model', 'year', 'price', 'image_left', 'image_right',
            'image_front', 'image_back', 'image_side', 'habitacl',
            'category', 'km', 'Puissance_fiscale', 'Origine',
            'Première_main', 'status', 'Boite_de_vitesses'
        ]
        widgets = {
            'Origine': forms.Select(attrs={'class': 'form-control'}),
            'Première_main': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'Boite_de_vitesses': forms.Select(attrs={'class': 'form-control'}),
        }