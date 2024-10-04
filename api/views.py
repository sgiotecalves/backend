from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Produto
from .serializer import ProdutoSerializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def listar_produtos(request):
    if request.method == 'GET':
        queryset = Produto.objects.all()
        serializer = ProdutoSerializers(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)