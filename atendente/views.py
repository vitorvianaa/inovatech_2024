from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Descarte, Resgate
from cliente.models import Solicitacao
from equipe_coleta.models import ChamadoColeta

# cadastrando um descarte
def cadastrar_descarte(request):
    if request.method == 'POST':
        dados = request.POST
        coleta = dados['porte_coleta']
        if coleta == 'pequeno':
            cesta = 'economica'
        elif coleta == 'medio':
            cesta = 'completa'
        elif coleta == 'grande':
            cesta = 'premium'

        descarte = Descarte.objects.create(
            material = dados['tipo_material'], porte_coleta = dados['porte_coleta'],
            cpf = dados['cpf_solicitante'], nome = dados['nome_solicitante'],
            email = dados['email_solicitante'], status = 'CRIADA'
        )
        resgate = Resgate.objects.create(tipo_cesta = 'GRANDE', quantidade = 2, cpf = dados['cpf_solicitante'], nome = dados['nome_solicitante'], 
                                         status = 'CRIADA'
                                         )
        return render(request, 'sucesso_descarte.html', {'dados': descarte.email})
    elif request.method == 'GET':
        return render(request, 'cadastrar_descarte.html')


# vizualizando todas as solicitações em aberto
def vizualizar_solicitacoes(request):
    if request.method == 'GET':
        status = request.GET.get('status', '')
        if status:
            solicitacoes = Solicitacao.objects.filter(status = status)
        else:
            solicitacoes = Solicitacao.objects.all() 
        return render(request, 'solicitacoes.html', {'dados': solicitacoes})


# exibindo os detalhes da solicitação
def detalhes_chamado(request, id):
    objeto = get_object_or_404(Solicitacao, id = id)
    return render(request, 'detalhes_chamado.html', {'chamado': objeto})

# alocando uma equipe para o descarte
def alocar_aquipe(request, id):
    objeto = get_object_or_404(Solicitacao, id = id)
    dados = request.POST
    chamado = ChamadoColeta.objects.create(solicitacao = objeto, equipe = dados['equipe'], status = objeto.status)
    objeto.equipe = dados['equipe']
    objeto.save()
    return render(request, 'sucesso_atendente.html')

def fechar_task(request, id):
    if request.method == 'POST':
        dados = request.POST
        obj = get_object_or_404(Solicitacao, id = id)
        obj.status = dados['status']
        obj.save()
        resgate = Resgate.objects.create(tipo_cesta = 'GRANDE', quantidade = 2, cpf = obj.cpf_solicitante, nome = obj.nome_solicitante, 
                                         status = 'CRIADA'
                                         )
        return render(request, 'sucesso_atendente.html')

def exibir_resgate(request):
    if request.method == 'GET':
        status = request.GET.get('status', '')
        if status:
            resgates = Resgate.objects.filter(status = status)
        else:
            resgates = Resgate.objects.all()
        return render(request, 'resgates.html', {'resgate': resgates})

def detalhes_resgate(request, id):
        resgate = get_object_or_404(Resgate, id = id)
        return render(request, 'detalhes_resgate.html', {'resgate': resgate})