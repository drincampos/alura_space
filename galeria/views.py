from django.shortcuts import render
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.filter(publicada=True)
    return render(request, 'index.html', {"cards": fotografias})

def imagem(request):
    return render(request, 'imagem.html')