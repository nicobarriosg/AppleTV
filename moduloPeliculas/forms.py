from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['tipo', 'nombre', 'genero', 'clasificacion', 'duracion', 'resena', 'imagen']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la película'}),
            'tipo': forms.Select(attrs={'class': 'form-control w-100', 'style': 'display: block; margin-bottom: 15px;'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo de duración en minutos'}),
            'resena': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve reseña del contenido de la película'}),
            'imagen': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL de la imagen'}),
        }

