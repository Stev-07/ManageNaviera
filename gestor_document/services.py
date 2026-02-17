from django.shortcuts import get_object_or_404
from gestor_document.models import Documento, Documento_pdf, Escala, Ruta
from django.db.models import Q

#function returns rutas query, for tracking
def get_rutas_para_naviero(filtro):
    if filtro:
        try:
            doc = Documento.objects.get(id = filtro)
            rutas = Ruta.objects.filter(id = doc.escala.ruta.id)
            return rutas, None
        except Documento.DoesNotExist:
            return None, "El registro buscado no existe"
    else:
        return Ruta.objects.all(), None

#fuction that return the scales destined for a port
def get_scales_for_port(filtro, pto):
    if filtro:
        try:
            doc = Documento.objects.get(id = filtro)
            if doc.escala.puertoDestino.id == pto:
                escalas = Escala.objects.filter(id = doc.escala.puertoDestino.id)
                return escalas, None
            else:
                return None, "El registro no se encuentra disponible"
        except:
            return None, "El registron no se encuentra disponible"
    else:
        escalas = Escala.objects.filter(Q(puertoDestino = pto) & (Q(documentos__estado = "pendiente")|Q(documentospdf__estado = "pendiente"))).distinct
        return escalas, None
    
#Funcion que retorna documentos, los de una escala o los de toda una ruta
#dependiendo del valor isscale, donde 1 representa "si"
def get_documents(isscale, id_value):
    if isscale == "1":
        escala = get_object_or_404(Escala, pk = id_value)
        ruta = escala.ruta.id
        documentos = Documento.objects.filter(escala = id_value)
        documentos2 = Documento_pdf.objecs.filter(escala = id_value)
        return {
            'documentos': documentos,
            'documentos2': documentos2,
            'ruta': ruta,
            'is_scale': True,
            'es_naviero': True,
        }
    else:
        documentos = Documento.objects.filter(escala__ruta = id_value)
        documentos2 = Documento_pdf.objects.filter(escala__ruta = id_value)
        return{
            'documentos': documentos,
            'documentos2': documentos2,
            'ruta': id_value,
            'is_scale': False,
            'es_naviero': True,
        }
    
#funcion que retorna los documentos que un portuario aprobará, el id recibido es el de su puerto
def get_documents_for_port(id_value):
    documentos = Documento.objects.filter(escala = id_value)
    documentospdf = Documento_pdf.objects.filter(escala = id_value)
    return{
        'documentos': documentos,
        'documentos2': documentospdf,
        'esc': id_value,
    }


           
