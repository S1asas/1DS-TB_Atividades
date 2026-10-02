from rest_framework.serializers import ModelSerializer
from .models import categoria

class categoriaserializer(ModelSerializer):
    class meta:
        model= categoria
        fields = '__all__'
        