from django.shortcuts import render
from .models import Curso

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

#url - view - html
def homecursos(request):
    context = {}
    lista_cursos = Curso.objects.all()
    context['lista_cursos'] = lista_cursos
    return render(request, 'homecursos.html')