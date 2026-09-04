from django.db import models
# Create your models here.
class categoria (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome 