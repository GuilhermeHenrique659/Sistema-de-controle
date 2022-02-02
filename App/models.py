from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class solicitacao(models.Model):
    STATUS = (
        ('Aguardar','Aguardar'),
        ('Respondido','Respondido'),
        ('Concluido','Concluido')
    )
    nome_do_consultor = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=255,null=False)
    quadra = models.CharField(max_length=255,null=False)
    lote = models.CharField(max_length=255,null=False)
    data = models.DateField(null=False)
    mensagem = models.TextField(null=False)
    respota = models.TextField(null=True)
    status = models.CharField(max_length=255, choices=STATUS ,null=False, default='Aguardar')
    def __str__(self):
        return self.cliente