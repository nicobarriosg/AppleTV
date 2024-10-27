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
        ('Animacion', 'Animacion'),
        ('Ciencia ficcion', 'Ciencia ficción'),
        ('Documental', 'Documental'),
        ('Animacion', 'Animación'),
    ]

    CLASIFICACION_CHOICES = [
        ('TE', 'TE'),
        ('TE+7', 'TE+7'),
        ('14+', '14+'),
        ('18+', '18+'),
    ]

    nombre = models.CharField(max_length=50, help_text='Nombre de la película')
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES,
                            help_text='Género de la película', blank=False)
    clasificacion = models.CharField(
        max_length=8, choices=CLASIFICACION_CHOICES, help_text='Clasificación de la película', blank=False)
    año = models.PositiveIntegerField(help_text='Año de publicacion')
    duracion = models.PositiveIntegerField(help_text='Duración de la película en minutos')
    resena = models.TextField(blank=True, help_text='Breve reseña del contenido de la película')
    imagen = models.URLField()  # Aquí se almacena la URL de la imagen

    def __str__(self):
        return self.nombre


class Serie(models.Model):

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
        ('Animacion', 'Animacion'),
        ('Ciencia ficcion', 'Ciencia ficción'),
        ('Documental', 'Documental'),
        ('Animacion', 'Animación'),
    ]

    CLASIFICACION_CHOICES = [
        ('TE', 'TE'),
        ('TE+7', 'TE+7'),
        ('14+', '14+'),
        ('18+', '18+'),
    ]

    nombre = models.CharField(max_length=50, help_text='Nombre de la serie')
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES,
                            help_text='Género de la serie', blank=False)
    clasificacion = models.CharField(
        max_length=8, choices=CLASIFICACION_CHOICES, help_text='Clasificación de la serie', blank=False)
    año = models.PositiveIntegerField(help_text='Año de publicacion')
    temporadas = models.PositiveIntegerField(help_text='Número de temporadas')
    capitulos = models.PositiveIntegerField(help_text='Número de capítulos por temporada')
    resena = models.TextField(blank=True, help_text='Breve reseña del contenido de la serie')
    imagen = models.URLField()  # Aquí se almacena la URL de la imagen

    def __str__(self):
        return self.nombre
