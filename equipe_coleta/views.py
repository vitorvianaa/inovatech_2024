from django.shortcuts import render, get_object_or_404, redirect
from .models import ChamadoColeta
from django.http import HttpResponse
from cliente.models import Solicitacao

def exibir_tasks(request):
    if request.method == 'GET':
        dados = ChamadoColeta.objects.all()
        return render(request, 'dashboard.html', {'dados': dados})


def detalhe_task(request, id):
    if request.method == 'GET':
        dados = get_object_or_404(ChamadoColeta, id = id)
        return render(request, 'detalhes_task.html', {'chamado': dados})


def mudar_status(request, id):
    if request.method == 'POST':
        dados = request.POST
        status = dados['status']
        atualizado = ChamadoColeta.objects.filter(id = id).update(status = status)
        solicitacao = ChamadoColeta.objects.get(id = id)
        solicitacao_att = Solicitacao.objects.filter(id = solicitacao.solicitacao.id).update(status = status)
        return redirect('exibir_tasks')