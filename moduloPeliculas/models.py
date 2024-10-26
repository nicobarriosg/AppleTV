from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Pelicula(models.Model):

    GENERO_CHOICES = [
        ('Accion', 'Acción'),
        ('Comedia', 'Comedia'),
        ('Drama', 'Drama'),
        ('Suspenso', 'Suspenso'),
        ('Crimen', 'Crimen'),
        ('Romance', 'Romance'),
        ('Terror', 'Terror'),
        ('Musical', 'Musical'),
        ('Aventura', 'Aventura'),

    ]

    CLASIFICACION_CHOICES = [
        ('TE', 'TE'),
        ('TE+7', 'TE+7'),
        ('14+', '14+'),
        ('18+', '18+'),
    ]

    TIPO_CHOICES = [
        ('pelicula', 'Película'),
        ('serie', 'Serie'),
    ]

    nombre = models.CharField(max_length=50, help_text='Nombre de la película')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, help_text='Pelicula o Serie')
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES,
                            help_text='Género de la película', blank=False)
    clasificacion = models.CharField(
        max_length=8, choices=CLASIFICACION_CHOICES, help_text='Clasificación de la película', blank=False)
    duracion = models.PositiveIntegerField(
        help_text='Tiempo de duración en minutos')
    resena = models.TextField(
        blank=True, help_text='Breve reseña del contenido de la película')
    imagen = models.URLField()  # Aquí se almacena la URL de la imagen



    def __str__(self):
        return self.nombre
