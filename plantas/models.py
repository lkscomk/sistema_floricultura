from django.db import models
from django.contrib.auth.models import User

class Plantas(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    disponibilidade = models.BooleanField(default=True)
    quantidade_estoque = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    observacoes = models.TextField()

    def __str__(self):
        return self.nome
