from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=60)
    def __str__(self):
        return self.nome

    descricao = models.CharField(max_length=60)
    def __str__(self):
        return self.descricao

    preco = models.FloatField(max_length=60)
    def __str__(self):
        return self.preco

    quantidade = models.IntegerField(max_length=60)
    def __str__(self):
        return self.quantidade

