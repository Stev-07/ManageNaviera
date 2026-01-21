from django import forms
from .models import Ruta, Escala, Documento

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

