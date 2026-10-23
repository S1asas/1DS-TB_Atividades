from django.shortcuts import render
from .models import categoria, Produto
from rest_framework.decorators import api_view
from .serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET' , 'POST'])
def listar_categorias(request):         
    if request.method == 'GET':
        queryset = categoria.objects.all()
        Serializers = CategoriaSerializer(queryset, many=True)
        return Response(Serializers.data)
    elif request.method == 'POST':
        Serializers = CategoriaSerializer(data=request.data)
        if Serializers.is_valid():
            Serializers.save()
            return Response(Serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET' , 'POST'])
def listar_produtos(request):         
    if request.method == 'GET':
        queryset = Produto.objects.all()
        Serializers = ProdutoSerializer(queryset, many=True)
        return Response(Serializers.data)
    elif request.method == 'POST':
        Serializers = ProdutoSerializer(data=request.data)
        if Serializers.is_valid():
            Serializers.save()
            return Response(Serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)        
    @api_view(['GET' , 'PATCH'])
    def detalhe_produto(request, pk):
        