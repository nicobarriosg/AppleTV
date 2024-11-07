from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Serie
from .forms import PeliculaForm, SerieForm
from django.contrib import messages

def pagina_principal(request):
    # Filtra películas y series de drama
    peliculas_drama = Pelicula.objects.filter(genero='Drama')
    series_drama = Serie.objects.filter(genero='Drama')

    # Obtiene todas las series
    series = Serie.objects.all()

    # Últimos estrenos (año 2024)
    estrenos_peliculas = Pelicula.objects.filter(año=2024)
    estrenos_series = Serie.objects.filter(año=2024)
    ultimos_estrenos = list(estrenos_peliculas) + list(estrenos_series)
    ultimos_estrenos.sort(key=lambda x: x.nombre)

    # "Nuestro Asombroso Planeta" (género documental)
    documentales_peliculas = Pelicula.objects.filter(genero='Documental')
    documentales_series = Serie.objects.filter(genero='Documental')
    documentales = list(documentales_peliculas) + list(documentales_series)

    # "Todas las Películas"
    todas_peliculas = Pelicula.objects.all()

    # "Comedia: Todas las Series" (género comedia)
    series_comedia = Serie.objects.filter(genero='Comedia')

    # "No Ficción: Todas las Series" (todas las series excepto ficción)
    series_no_ficcion = Serie.objects.exclude(genero='Ciencia ficcion')

    # "Todo para Toda la Familia" (películas y series de animación)
    contenido_familiar_peliculas = Pelicula.objects.filter(genero='Animacion')
    contenido_familiar_series = Serie.objects.filter(genero='Animacion')
    contenido_familiar = list(contenido_familiar_peliculas) + list(contenido_familiar_series)

    return render(request, 'main.html', {
        'peliculas_drama': peliculas_drama,
        'series_drama': series_drama,
        'series': series,
        'ultimos_estrenos': ultimos_estrenos,
        'documentales': documentales,
        'todas_peliculas': todas_peliculas,
        'series_comedia': series_comedia,
        'series_no_ficcion': series_no_ficcion,
        'contenido_familiar': contenido_familiar,
    })




def PeliculaListView(request):

    peliculas = Pelicula.objects.all()

    peliculas = peliculas.order_by('nombre')

    peliculas = {"peliculas":peliculas}

    return render(request,"peliculas_list.html",peliculas)

def PeliculaListCrud(request):

    peliculas = Pelicula.objects.all()

    peliculas = peliculas.order_by('nombre')

    peliculas = {"peliculas":peliculas}

    return render(request,"peliculas_crud.html",peliculas)

def pelicula_detail(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, "pelicula_details.html", {'pelicula': pelicula})


def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # Redirige a la vista lista_articulos
            return PeliculaListView(request)
    else:
        form = PeliculaForm()

    return render(request, "pelicula_form.html", {'form': form})

def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    # Agrega un mensaje de confirmación
    messages.success(
        request, f'Se ha eliminado a {pelicula.nombre}')
    return redirect('pagina_principal')

def editar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            print("Formulario válido. Película guardada.")
            return redirect('pagina_principal')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = PeliculaForm(instance=pelicula)

    return render(request, 'pelicula_form.html', {'form': form})



def SerieListView(request):
    series = Serie.objects.all()
    series = series.order_by('nombre')
    context = {"series": series}
    return render(request, "series_list.html", context)

def SerieListCrud(request):
    series = Serie.objects.all()
    series = series.order_by('nombre')
    context = {"series": series}
    return render(request, "series_crud.html", context)

def serie_detail(request, id):
    serie = get_object_or_404(Serie, id=id)
    return render(request, "serie_details.html", {'serie': serie})

def agregar_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return SerieListView(request)
    else:
        form = SerieForm()
    return render(request, "serie_form.html", {'form': form})

def eliminar_serie(request, id):
    serie = Serie.objects.get(id=id)
    serie.delete()
    messages.success(request, f'Se ha eliminado a {serie.nombre}')
    return redirect('pagina_principal')

def editar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES, instance=serie)
        if form.is_valid():
            form.save()
            print("Formulario válido. Serie guardada.")
            return redirect('pagina_principal')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = SerieForm(instance=serie)
    return render(request, 'serie_form.html', {'form': form})
