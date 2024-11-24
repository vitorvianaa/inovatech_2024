from .views import cadastrar_descarte, vizualizar_solicitacoes, detalhes_chamado, alocar_aquipe
from django.urls import path


urlpatterns = [
    path('descarte/', cadastrar_descarte, name='cadastro'),
    path('solicitacoes/', vizualizar_solicitacoes, name='solicitacao'),
    #path('solicitacoes/filtro/', filtrar_status, name = 'filtrar_status'),
    path('solicitacoes/<int:id>/', detalhes_chamado, name='detalhes_chamado'),
    path('coleta/<int:id>', alocar_aquipe, name='alocar_equipe')
]