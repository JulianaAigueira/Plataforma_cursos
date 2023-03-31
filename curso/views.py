from django.shortcuts import render
from .models import Curso
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
#def homepage(request):
#    return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'


#url - view - html
#def homecursos(request):
#    context = {}
#    lista_cursos = Curso.objects.all()
#    context['lista_cursos'] = lista_cursos
#    return render(request, 'homecursos.html', context)


class Homecursos(ListView):
    template_name = 'homecursos.html'
    model = Curso
    # object_list -> lista de itens do modelo

class Detalhescurso(DetailView):
    template_name = 'detalhescurso.html'
    model = Curso
    # object -> 1 item do nosso modelo