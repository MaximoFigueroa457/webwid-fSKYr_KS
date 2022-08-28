from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

def pagina(request):
    return render(request, 'paginas/page.html')

def plantas(request):
    return render(request, 'plantas/index.html')

def crear(request):
    return render(request, 'plantas/crear.html')

def editar(request):
    return render(request, 'plantas/editar.html')