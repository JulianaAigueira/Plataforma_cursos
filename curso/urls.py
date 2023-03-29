# url - view - template

from django.urls import path, include
from .views import homepage, homecursos

urlpatterns = [
    path('', homepage),
    path('cursos/', homecursos)
]
