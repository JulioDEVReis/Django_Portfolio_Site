from django.shortcuts import render, get_object_or_404
from .models import Projetos

def home(request):
    projetos = Projetos.objects.all()
    return render(request, 'home.html', {'projetos': projetos})

def blog(request):
    pass

def portfolio(request, projeto_id):
    projetos = Projetos.objects.all()
    projeto = get_object_or_404(Projetos, pk=projeto_id)
    return render(request, 'portfolio.html', {'projetos': projetos, 'projeto': projeto})

