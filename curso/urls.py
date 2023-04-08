# url - view - template

from django.urls import path, reverse_lazy
from .views import Homecursos, Homepage, Detalhescurso, Pesquisacurso, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view

app_name= 'curso'


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('cursos/', Homecursos.as_view(), name='homecursos'),
    path('cursos/<int:pk>', Detalhescurso.as_view(), name='detalhescurso'),
    path('pesquisa/', Pesquisacurso.as_view(), name='pesquisacurso'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/',auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('curso:homecursos')), name='mudarsenha'),
]
