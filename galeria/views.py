from django.shortcuts import render
from galeria.models import Fotografia

def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina", "legenda": "webbtelecope.org / NASA / James Webb"},
        2: {"nome": "Galáxia NGC 1079", "legenda": "nasa.org / NASA / Hubble"}
    }
    fotografias = Fotografia.objects.all()
    return render(request, 'index.html', {"cards": fotografias})

def imagem(request):
    return render(request, 'imagem.html')