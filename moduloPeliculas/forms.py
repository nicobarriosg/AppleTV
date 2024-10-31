from django import forms
from .models import Pelicula, Serie

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'genero', 'clasificacion', 'año', 'duracion', 'resena', 'imagen', 'imagenbanner']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la película'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de publicación'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración en minutos'}),
            'resena': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve reseña del contenido de la película'}),
            'imagen': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL de la imagen'}),
            'imagenbanner': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL del banner de la imagen'}),
        }

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['nombre', 'genero', 'clasificacion', 'año', 'temporadas', 'capitulos', 'resena', 'imagen', 'imagenbanner']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la serie'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de publicación'}),
            'temporadas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de temporadas'}),
            'capitulos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de capítulos por temporada'}),
            'resena': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve reseña del contenido de la serie'}),
            'imagen': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL de la imagen'}),
            'imagenbanner': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL del banner de la imagen'}),
        }
