from rest_framework import serializers
from .models import Produto

class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'id',
            'codigoProduto',
            'tituloProduto',
            'preco',
            'descricao',
            'imagemProduto',
            'categoriaProduto',
            'exibirHome',
        ]
