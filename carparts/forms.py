from django import forms
from .models import Vehicle

class VehicleMultiFilterForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['marque', 'model_name', 'engine', 'year']
        widgets = {
            'marque': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marque'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modèle'}),
            'engine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Moteur'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Année'}),
        }
