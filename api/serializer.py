from rest_framework import serializers
from .models import Produto

class ProdutoSerializers(serializers.modelSerializers):
    class Meta:
        model = Produto
        fiels = [
            'id',
            'codigoProduto',
            'tituloProduto',
            'preco',
            'descricao',
            'imagemProduto',
            'categoriaProduto',
            'exibirHome',

        ]

