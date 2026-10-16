from django.db import models
# Create your models here.
class categoria (models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome 

class Produto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True,null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveBigIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT, related_name="Produtos")

    def __str__(self):
        return self.nome