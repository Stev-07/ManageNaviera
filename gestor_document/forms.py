from django import forms
from .models import Ruta, Escala, Documento, Documento_pdf

class billOfLading(forms.Form):
    tipo = forms.CharField(max_length=200)
    infovendedor = forms.CharField(max_length=200)

class viajeForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['fechaSalida', 'nave']

class escalaForm(forms.ModelForm):
    class Meta:
        model = Escala
        fields = ['nombre', 'puertoDestino']

class documentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['tipo', 'infovendedor']

class documentopdfForm(forms.ModelForm):
    class Meta:
        model = Documento_pdf
        fields = ['nombre', 'tipo', 'archivo']
