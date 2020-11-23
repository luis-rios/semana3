from django.shortcuts import render

from clase.models import Clase


def get_clases(request):
    response = ''
    clases = Clase.objects.all()
    return render(request, 'clases/lista.html', {'clases': clases})


def get_clase(request, clase_id):
    clase = Clase.objects.get(id=clase_id)
    return render(request, 'clases/detalle.html', {'clase': clase})
