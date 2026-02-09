from django.urls import path
from django.urls import path
from .views import CustomLoginView
from . import views #esto importa los archivos de la app en la que nos encontramos
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

#esto es importante para mantener las urls en sus apps respectivas 
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', RedirectView.as_view(url='/login/')),
    path('index/', views.helloWorld, name= 'index'),
    path('create_viaje/', views.create_viajee, name='viaje'),
    path('create_bol/<int:idscale>/<int:idrut>/', views.create_BOL, name='bill'),
    path('create_scale/<int:idrut>/', views.create_scale, name='scale'),
    path('viaje_scale/<int:id>/', views.viaje_scale, name='viaje_scale'),
    path('upload_pdf/<int:idscale>/<int:idrut>/', views.upload_pdf, name= 'pdf'),
    path('view_document/<int:idscale>/<int:idrut>/<int:iddoc>/', views.view_pdf, name='view_pdf'),
    path('all_docs/', views.view_all, name='view_all'),
    path('pdf/<int:iddoc>/', views.download_to_pdf, name='download_to_pdf'),
    path('delete/<int:idrut>/', views.delete_rut, name='deleterut'),
    path('aprobar_doc/<int:iddoc>/', views.aprobar_doc, name='aprobar_doc'),
    path('track/', views.track, name='track'),
    path('logout/', LogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)