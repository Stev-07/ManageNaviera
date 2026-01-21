from django.urls import path
from . import views #esto importa los archivos de la app en la que nos encontramos

#esto es importante para mantener las urls en sus apps respectivas 
urlpatterns = [
    path('', views.helloWorld ,name= 'index'),
    path('create_viaje/', views.create_viajee, name='viaje'),
    path('create_bol/<int:idscale>/<int:idrut>/', views.create_BOL, name='bill'),
    path('create_scale/<int:idrut>/', views.create_scale, name='scale'),
    path('viaje_scale/<int:id>/', views.viaje_scale, name='viaje_scale'),
]