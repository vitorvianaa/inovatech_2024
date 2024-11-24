from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=6)

    def __str__(self):
        return f'Rua: - {self.rua}, CEP - {self.cep}'

class Solicitacao(models.Model):
    tipo_material = models.CharField(max_length=255)
    nome_solicitante = models.CharField(max_length=255)
    cpf_solicitante = models.CharField(max_length=11)
    numero_contato = models.CharField(max_length=12)
    email_solicitante = models.EmailField()
    status = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    foto_coleta = models.ImageField()
    equipe = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Solicitação - {self.id}'
