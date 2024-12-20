from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Solicitacao, Endereco
from atendente.models import Resgate, PontosColeta

def home(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    elif request.method == 'POST':
        dados = request.POST
        foto = request.FILES['foto_coleta']
        nome = dados['nome_solicitante']
        tipo_material = dados['tipo_material']
        cpf = dados['cpf_solicitante']
        numero_contato = dados['numero_contato']
        email = dados['email_solicitante']
        rua = dados['rua']
        cep = dados['cep']
        numero = dados['numero']

        endereco = Endereco.objects.create(rua = rua, cep = cep, numero = numero)
        solicitacao = Solicitacao.objects.create(nome_solicitante = nome, tipo_material = tipo_material,
                                                 cpf_solicitante = cpf, numero_contato = numero_contato,
                                                 email_solicitante = email, endereco = endereco, foto_coleta = foto, status = 'CRIADA'
                                                 )
        return render(request, 'sucesso.html')


def pontos_coleta(request):
    if request.method == 'GET':
        pev = PontosColeta.objects.all()
        return render(request, 'teste.html', {'pev': pev})

def about(request):
    return render(request, 'about.html')


def servicos(request):
    return render(request, 'services.html')