from django.urls import path, include
from .views import  home, emprestar, devolver, aluno, livro, DelAluno, DelLivro, base

urlpatterns = [
    path('base/', base, name = 'base_url'),
    path('', home, name = 'home_url'),
    path('Emprestar/', emprestar, name = 'emprestar_url'),
    path('Cadastrar_Aluno/', aluno, name = 'aluno_url'),
    path('Cadastrar_Livro/', livro, name = 'livro_url'),
    path('Devolver/<int:id>/', devolver, name = 'devolver_url'),
    path('Del_Aluno/<int:id>/', DelAluno, name = 'delaluno_url'),
    path('Del_Livro/<int:id>/', DelLivro, name = 'dellivro_url'),

]
