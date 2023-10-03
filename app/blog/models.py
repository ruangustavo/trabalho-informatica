from autor.models import Autor
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]


class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-data_publicacao"]
        verbose_name_plural = "Postagens"
