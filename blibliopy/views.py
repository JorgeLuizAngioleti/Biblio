from django.shortcuts import render, redirect, HttpResponse
from .models import Biblioteca, Usuario, Emprestar
from . forms import EmprestarForm, CadastrarAluno, CadastrarLivro
from django.core.paginator import Paginator, InvalidPage, EmptyPage#paginaçoes
from django.contrib import messages#mensagens
def base (request):
    return render(request, 'bliblio/base.html')

def home(request):
    contact_list = Emprestar.objects.all()
    paginator = Paginator(contact_list, 10) # Mostra 25 contatos por página
    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)

    return render(request,'bliblio/home.html',{'contacts': contacts})


def emprestar(request):
    dados = {}
    x = request.GET.get("aluno")
    c = request.GET.get("livro")
    try:
        aluno = Usuario.objects.filter(codigo=x)
        livro = Biblioteca.objects.filter(codigo=c)
        for a in aluno:
            print(a.nome)
        for l in livro:
            print(l.livro)

        form = EmprestarForm(request.POST or None, initial={'codigo_livro':l.livro,'codigo_aluno':a.nome})
        if aluno and livro:
            print('ele existe',aluno,livro)
            if form.is_valid():
                form.save()
                salvos={}
                salvos['aluno']=aluno
                salvos['livro']=livro
                return render(request,'bliblio/sucesso.html',salvos)

        dados['form'] = form
    except:
        dados['mensagem'] = 'Aluno ou livro não existe!!!'
    return render(request,'bliblio/form.html', dados)

def devolver(request, id):
    dev = Emprestar.objects.get(pk=id)
    if request.method == 'POST':
        dev.delete()
        return redirect("home_url")
    return render(request,'bliblio/deletar.html',{'pega':dev})


def aluno(request):
    dados={}
    alunos = Usuario.objects.all()
    form = CadastrarAluno(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Aluno salvo com sucesso!')
        return redirect('aluno_url')
    dados['form']=form
    dados['alunos']=alunos
    return render(request,'bliblio/aluno_cad.html',dados)

def DelAluno(request, id):
    dado = Usuario.objects.get(pk=id)
    dado.delete()
    return redirect('aluno_url')

def DelLivro(request, id):
    dado = Biblioteca.objects.get(pk=id)
    dado.delete()
    return redirect('livro_url')

def livro(request):
    dados={}
    livros = Biblioteca.objects.all()
    form = CadastrarLivro(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Livro salvo com sucesso!')
        return redirect('livro_url')
    dados['form']=form
    dados['livros']=livros
    return render(request,'bliblio/livro_cad.html',dados)

