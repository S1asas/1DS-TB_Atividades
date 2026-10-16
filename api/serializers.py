from rest_framework.serializers import ModelSerializer
from .models import categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model= categoria
        fields = '__all__'
