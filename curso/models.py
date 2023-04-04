from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


#criar o curso

LISTA_CATEGORIAS = (
    ('CORETE', 'Corte'),
    ('MODELAGEM', 'Modelagem'),
    ('COSTURA', 'Costura'),
    ('OUTROS', 'Outros'),
)

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_cursos')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# criar os episodios
class Episodio(models.Model):
    curso = models.ForeignKey('Curso', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.curso.titulo + " - " + self.titulo


#criar o usuário

class Usuario(AbstractUser):
    curso_vistos = models.ManyToManyField('Curso')
