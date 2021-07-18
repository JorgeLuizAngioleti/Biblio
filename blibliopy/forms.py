from django.forms import ModelForm
from .models import Emprestar, Usuario, Biblioteca

class EmprestarForm(ModelForm):
    class Meta:
        model = Emprestar
        fields = ['codigo_livro','codigo_aluno','turma']

class CadastrarAluno(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','codigo','escola']

class CadastrarLivro(ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['livro','codigo','detalhes']