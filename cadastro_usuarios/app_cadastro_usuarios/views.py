from django.shortcuts import render
from .models import Usuarios


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    # Salvar dados no banco de dados
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todos os usuarios ja cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuarios.object.all()
    }
    # Retornar os dados da página de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)
