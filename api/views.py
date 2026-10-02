from django.shortcuts import render
from .models import categoria
from rest_framework.decorators import api_view
from  .serializers import categoriaserializer
from rest_framework.response import Response

@api_view(['GET' , 'POST'])
def listar_categorias(request):         #para fazer requisições como o CRUD
    if request.method == 'GET':
        queryset = categoria.objects.all()
        serializers = categoriaserializer (queryset, many=True)
        return Response(serializers.data)