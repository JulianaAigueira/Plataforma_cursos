from .models import Curso

def lista_cursos_recentes(request):
    lista_cursos = Curso.objects.all().order_by('-data_criacao')[0:8]
    return {'lista_cursos_recentes': lista_cursos}


def lista_cursos_emalta(request):
    lista_cursos = Curso.objects.all().order_by('-visualizacoes')[0:8]
    return {'lista_cursos_emalta': lista_cursos}
