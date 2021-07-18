from django.db import models
from datetime import date, datetime
class Biblioteca(models.Model):
    livro = models.CharField(max_length=50)
    codigo = models.CharField(max_length=100, unique=True)
    detalhes = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.livro


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=100, unique=True)
    escola = models.CharField(max_length=30)
    def __str__(self):
        return self.nome
AULAS = (
            ('p', 'Pré'),
            ('1a', '1º ano'),
            ('2a', '2º ano'),
            ('3a', '3º ano'),
            ('4a', '4º ano'),
            ('5a', '5º ano'),
            ('6a', '6º ano'),
            ('7a', '7º ano'),
            ('8a', '8º ano'),
            ('9a', '9º ano'),

        )
class Emprestar(models.Model):
    data =  models.DateField(auto_now_add=True)
    codigo_livro = models.CharField(max_length=100)
    codigo_aluno = models.CharField(max_length=100)
    validar = models.BooleanField(default=True)
    turma = models.CharField(u'Turma', max_length=3, choices=AULAS)
    def __str__(self):
        return 'codigo do aluno: '+self.codigo_aluno+' codigo livro: '+self.codigo_livro
