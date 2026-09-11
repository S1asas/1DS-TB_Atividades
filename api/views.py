from django.shortcuts import render
from .models import categoria
from rest_framework.decorators import api_view

@api_view('GET')
def listar_categorias(request):         #para fazer requisições como o CRUD
    if request.method == 'GET':
        queryset = categoria.objects.all()