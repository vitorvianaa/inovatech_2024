from .views import cadastrar_descarte, vizualizar_solicitacoes, detalhes_chamado, alocar_aquipe, fechar_task, exibir_resgate, detalhes_resgate
from django.urls import path


urlpatterns = [
    path('descarte/', cadastrar_descarte, name='cadastro'),
    path('solicitacoes/', vizualizar_solicitacoes, name='solicitacao'),
    #path('solicitacoes/filtro/', filtrar_status, name = 'filtrar_status'),
    path('solicitacoes/<int:id>/', detalhes_chamado, name='detalhes_chamado'),
    path('coleta/<int:id>', alocar_aquipe, name='alocar_equipe'),
    path('mudar-status/<int:id>/', fechar_task, name='fechar_task'),
    path('resgate/', exibir_resgate, name='exibir_resgate'),
    path('resgate/<int:id>/', detalhes_resgate, name='detalhes_resgate'),
]