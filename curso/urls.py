# url - view - template

from django.urls import path, include
from .views import Homecursos, Homepage, Detalhescurso, Pesquisacurso
app_name= 'curso'


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('cursos/', Homecursos.as_view(), name='homecursos'),
    path('cursos/<int:pk>', Detalhescurso.as_view(), name='detalhescurso'),
    path('pesquisa/', Pesquisacurso.as_view(), name='pesquisacurso')
]
