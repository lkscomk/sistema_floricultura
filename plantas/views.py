from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Plantas

@login_required
def index(request):
    return render(request, 'index.html', {'mensagem': 'Sistema Interno de Controle'})

@login_required
def excluir_planta(request, id):
    planta = get_object_or_404(Plantas, id=id)

    if request.method == 'POST':
        planta.delete()
        return redirect('lista_plantas')

    return render(request, 'excluir_planta.html', {'planta': planta})

def contatos(request):
    return render(request, 'contatos.html')

def sobre(request):
    return render(request, 'sobre.html')

@login_required #so pode acessa essa view se tiver logado
def editar_planta(request, id):
    planta = get_object_or_404(Plantas, id=id)
    usuarios = User.objects.all()
    if request.method == 'POST':
        print(request.POST)
        # Processar os dados do formulário e salvar as alterações
        planta.nome = request.POST.get('nome')
        planta.especie = request.POST.get('especie')
        disponibilidade = request.POST.get('disponibilidade', False)
        if disponibilidade.upper() == "SIM":
            disponibilidade = True
        else:
            disponibilidade = False
        planta.quantidade_estoque = request.POST.get('quantidade_estoque')
        planta.valor = request.POST.get('valor')
        planta.observacoes = request.POST.get('observacoes')
        planta.criado_por_id = request.POST.get('criado_por')
        planta.save()
        messages.success(request, 'Planta atualizada com sucesso.')
        return redirect('lista_plantas')
    return render(request, 'editar_planta.html', {'planta': planta, 'usuarios': usuarios})

@login_required #so pode acessa essa view se tiver logado
def incluir_planta(request):
    if request.method == 'POST':
        print(request.POST)
        nome = request.POST['nome']
        especie = request.POST['especie']
        disponibilidade = request.POST.get('disponibilidade', False)
        if disponibilidade.upper() == "SIM":
            disponibilidade = True
        else:
            disponibilidade = False
        quantidade_estoque = request.POST['quantidade_estoque']
        valor = request.POST['valor']
        observacoes = request.POST['observacoes']
        criado_por = request.user

        planta = Plantas(nome=nome, especie=especie, disponibilidade=disponibilidade, quantidade_estoque=quantidade_estoque, valor=valor, observacoes=observacoes, criado_por=criado_por)
        planta.save()

        return redirect('lista_plantas')

    usuarios = User.objects.all()
    conteudo = {'usuarios': usuarios}
    return render(request, 'incluir_planta.html', conteudo)

@login_required #so pode acessa essa view se tiver logado
def lista_plantas(request):
    plantas = Plantas.objects.all()
    return render(request, 'lista_plantas.html', {'plantas': plantas})

@login_required #so pode acessa essa view se tiver logado
def exibir_planta(request, id):
    planta = get_object_or_404(Plantas, id=id)
    usuarios = User.objects.all()
    item = {'planta': planta, 'usuarios': usuarios}
    return render(request, 'exibir_planta.html', item)

def login_app(request): #nao pode ser apenas LOGIN pq o codigo estava confundindo com o login da importacao
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redireciona para a página inicial após o login
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def logout_app(request):
    logout(request)
    return redirect('home')

def cadastro_app(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Realize a validação dos dados conforme necessário

        # Crie o usuário
        user = User.objects.create_user(username=username, email=email, password=password)

        # Faça o login do usuário
        login(request, user)

        # Redirecione para a página desejada após o cadastro
        return redirect('home')

    return render(request, 'cadastro.html')