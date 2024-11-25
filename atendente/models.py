from django.db import models
from cliente.models import Endereco

class Descarte(models.Model):
    material = models.CharField(max_length=255)
    porte_coleta = models.CharField(max_length=255) # porte = Pequeno, Medio, Grande
    cpf = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(max_length=100) #True == Valido || False == Invalido

    def __str__(self):
        return f'Id Resgate - {self.id}'

class Resgate(models.Model):
    #descarte = models.ForeignKey(Descarte, on_delete=models.CASCADE)
    tipo_cesta = models.CharField(max_length=255) # Pequeno = Econômica, Medio = Completa, Grande = Premium
    quantidade = models.IntegerField()
    cpf = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    status = models.CharField(max_length=100) 
    # quando criado : status == True -> posso resgatar
    # depois de resgatado: status == False -> não posso resgatar
    data_disponivel = models.DateField(auto_now_add=True) # dia que o descarte ficou disponivel
    data_resgate = models.DateField(auto_now=True) # dia que foi resgatado

    def __str__(self):
        return f'Id Resgate - {self.id}'
    
class PontosColeta(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=100, default='none')
    complemento = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome