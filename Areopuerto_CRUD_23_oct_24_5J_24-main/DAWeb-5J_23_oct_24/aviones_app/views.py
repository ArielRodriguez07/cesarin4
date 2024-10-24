from django.shortcuts import render

# Create your views here.
def listadoAviones(request):
    return render(request,"gestionarAviones.html")
