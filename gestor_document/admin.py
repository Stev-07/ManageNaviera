from django.contrib import admin
from .models import Escala,Ruta,Documento,Nave, Puerto

# Register your models here.
admin.site.register(Escala)
admin.site.register(Ruta)
admin.site.register(Puerto)
admin.site.register(Nave)
admin.site.register(Documento)
