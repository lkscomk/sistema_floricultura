from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Plantas

@login_required
def index(request):
    return render(request, 'index.html', {'mensagem': 'Sistema Interno de Controle'})

def contatos(request):
    return render(request, 'contatos.html')

def sobre(request):
    return render(request, 'sobre.html')

def error_404(request, exception):
    return render(request, '404.html', status=404)

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