from django.shortcuts import render
from .models import categoria
from rest_framework.decorators import api_view
from .serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET' , 'POST'])
def listar_categorias(request):         #para fazer requisições como o CRUD
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
