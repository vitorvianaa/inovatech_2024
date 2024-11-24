from django.db import models
from cliente.models import Solicitacao

STATUS_CHOICES = [
    ('CRIADA', 'CRIADA'),
    ('EM ANDAMENTO', 'EM ANDAMENTO'),
    ('INCOMPLETA', 'INCOMPLETA'),
    ('SUCESSO', 'SUCESSO'),
    ('FALHA', 'FALHA'),
    ('PENDENTE', 'PENDENTE'),
    ('FECHADO', 'FECHADO')
]

class ChamadoColeta(models.Model):
    STATUS_CHOICES = [
    ('CRIADA', 'CRIADA'),
    ('EM ANDAMENTO', 'EM ANDAMENTO'),
    ('INCOMPLETA', 'INCOMPLETA'),
    ('SUCESSO', 'SUCESSO'),
    ('FALHA', 'FALHA'),
    ('PENDENTE', 'PENDENTE'),
    ('FECHADO', 'FECHADO')
]
    
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    equipe = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    data_inicial = models.DateField(auto_now_add=True)
    data_final = models.DateField(auto_now=True)


    def __str__(self):
        return self.equipe