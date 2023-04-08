from django.shortcuts import render,redirect, reverse
from .models import Curso, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
#def homepage(request):
#    return render(request, 'homepage.html')

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: # usuário está autenticado:
            return redirect('curso:homecursos') # redireciona para a homecursos
        else:

            return super().get(request, *args, **kwargs)# redirecionando para a homepage

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('curso:login')
        else:
            return reverse('curso:criarconta')



#url - view - html
#def homecursos(request):
#    context = {}
#    lista_cursos = Curso.objects.all()
#    context['lista_cursos'] = lista_cursos
#    return render(request, 'homecursos.html', context)


class Homecursos(LoginRequiredMixin, ListView):
    template_name = 'homecursos.html'
    model = Curso
    # object_list -> lista de itens do modelo




class Detalhescurso(LoginRequiredMixin, DetailView):
    template_name = 'detalhescurso.html'
    model = Curso
    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # descobrir qual o curso ele está acessando
        curso = self.get_object()
        # somar 1 nas visualizações daquele cursos
        curso.visualizacoes += 1
        # salvar
        curso.save()
        usuario = request.user
        usuario.curso_vistos.add(curso)

        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final


    def get_context_data(self, **kwargs):
        context = super(Detalhescurso, self).get_context_data(**kwargs)
        #filtra a tabelas de cursos pegando os cursos cuja categoria é igual a categoria do filme da página (object)
        #self.get_object()
        cursos_relacionados = Curso.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['cursos_relacionados'] = cursos_relacionados
        return context

class Pesquisacurso(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Curso

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('curso:homecursos')


class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('curso:login')
