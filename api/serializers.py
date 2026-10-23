from rest_framework.serializers import ModelSerializer
from .models import categoria, Produto


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model= categoria
        fields = '__all__'

class ProdutoSerializer(ModelSerializer):
    class Meta: 
        model = Produto
        fields = '__all__'