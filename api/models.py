from django.db import models

class produto (models.Model):
    codigoProduto = models.IntegerField_(maz_length=10)
    codigoProduto = models.CharField.(max_length=255)
    preço = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=500)
    categoriaProduto = models.CharField(max_length=255)
    imagemProduto = models.CharField(max_length=255)
    classProduto = models.CharField(max_length=255)
    exibirHome = models.BooleanField(default=True)