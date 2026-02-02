from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from .forms import billOfLading, viajeForm, documentoForm, escalaForm, documentopdfForm
from .models import Escala, Ruta, Nave, Documento, perfilUser
from django.template.loader import render_to_string
from xhtml2pdf import pisa

# Create your views here.
def helloWorld(request):
    return render(request, 'index.html')

#esta parte van los documentos, de momento es un ejemplo que puede extenderse al numero de documentos que se necesite
#en este caso son 3, pero solo cree un form para funcionamiento
def create_BOL(request, idscale, idrut):
    if request.method == 'GET':
        form = billOfLading()
        return render(request, './Documents/create_bol.html', {
            'form': form
        })
    else:
      ruta = get_object_or_404(Ruta, pk = idrut)
      escala = get_object_or_404(Escala, pk = idscale)
      buque = ruta.nave
      nave = get_object_or_404(Nave, pk = buque.id)
      form = documentoForm(request.POST)

      print(request.POST['infovendedor'])
      if form.is_valid():
          document = form.save(commit=False)
          document.nombreBuque = nave.nombre
          document.escala = escala
          document.save()
          return redirect('viaje_scale', idrut)
      else:
          print(form.errors)
          return HttpResponse("fallo algo")

def create_viajee(request):
    if request.method == 'POST':
        forma = viajeForm(request.POST)
        print("se creo")
        print(request.POST['nave'])
        print(request.POST['fechaSalida'])
        if forma.is_valid():
            print("si llego")
            ruta = forma.save()
            rutaid= ruta.id
            return redirect('viaje_scale', id=rutaid)
        else:
            print(forma.errors)
            messages.error(request, "El formulario es invalido, intente de nuevo")
            return HttpResponse("El formulario es invalido")
    else:
        form = viajeForm()
        return render(request, './Documents/create_viaje.html', {
            'form': form
        })

def viaje_scale(request, id):
    if request.method == 'GET':
        scales = Escala.objects.filter(ruta=id)
        context = {
            'scales' : scales,
            'idrut' : id
        }
        print(context)
        return render(request, './Documents/viaje_scale.html', context)
    else:
        return HttpResponse("en proceso")

def create_scale(request, idrut):
    if request.method == 'POST':
        form = escalaForm(request.POST)
        ruta = get_object_or_404(Ruta, pk = idrut)
        if form.is_valid():
            escala = form.save(commit=False)
            escala.ruta = ruta
            escala.save()
            print("guardado escala")
            return redirect('viaje_scale', id = idrut)
        else:
            print(form.errors)
            return HttpResponse("algo fallo")
    else:
        form = escalaForm()        
        context = {
            'idrut' : idrut, 
            'form' : form,
        }
        return render(request, './Documents/create_scale.html', context)

def upload_pdf(request, idscale, idrut):
    if request.method == 'POST':
        escala = get_object_or_404(Escala, pk = idscale)
        form = documentopdfForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.save(commit=False)
            pdf.escala = escala
            pdf.save()
            return redirect('viaje_scale', idrut)
        else:
            print(form.errors)
            return HttpResponse("fallo algo")
    else:
        form = documentopdfForm()
        return render(request, './Documents/upload_pdf.html', {'form': form} )

def view_pdf(request, idscale, idrut, iddoc):
    documento = get_object_or_404(Documento, pk = iddoc)
    return render(request, './Documents/view_document.html', {'documento': documento, 'idscal': idscale, 'idrut': idrut})

def view_all(request, iduser):
    user = get_object_or_404(perfilUser, pk = iduser)
    if user.puerto:
        return
    else:
        return 


def download_to_pdf(request, iddoc):
    documento = get_object_or_404(Documento, pk = iddoc)
    html_string = render_to_string(
        './Documents/view_document.html',
        {'documento': documento}
    )

    html = render_to_string(
        './Documents/document_pdf.html',
        {'documento': documento}
    )

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        f'attachment; filename="{documento.tipo}-{documento.pk}.pdf"'
    )
    pisa.CreatePDF(html, dest=response)
    return response


    