from django.urls import path, re_path
from django.contrib import admin
from moduloPeliculas import views
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.pagina_principal, name='pagina_principal'),
    path('agregarpelicula/', views.agregar_pelicula, name='agregarpelicula'),
    path('editar/<int:id>/', views.editar_pelicula, name='editar-pelicula'),
    path('eliminar/<int:id>/', views.eliminar_pelicula, name='eliminar-pelicula'),
    path('gestionpeliculas/', views.PeliculaListCrud, name='gestion_peliculas'),
    path('pelicula/<int:id>/', views.pelicula_detail, name='pelicula-detail'),

    
    path('agregarserie/', views.agregar_serie, name='agregarserie'),
    path('serie/<int:id>/', views.serie_detail, name='serie-detail'),
    path('editarserie/<int:id>/', views.editar_serie, name='editar-serie'),
    path('eliminarserie/<int:id>/', views.eliminar_serie, name='eliminar-serie'),
    path('gestionseries/', views.SerieListCrud, name='gestion_series'),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


