from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from .forms import billOfLading, viajeForm, documentoForm
from .models import Escala, Ruta, Nave

# Create your views here.
def helloWorld(request):
    return render(request, 'index.html')

def segudoHello(request):
    return HttpResponse("about you, i love everything")    

#esta parte van los documentos, de momento es un ejemplo
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
    return render (request, './Documents/create_scale.html')




    