# Generated by Django 5.1 on 2024-10-31 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloPeliculas', '0004_serie_remove_pelicula_tipo_pelicula_año_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='imagenbanner',
            field=models.URLField(blank=True, help_text='URL del banner de la imagen'),
        ),
        migrations.AddField(
            model_name='serie',
            name='imagenbanner',
            field=models.URLField(blank=True, help_text='URL del banner de la imagen'),
        ),
    ]
