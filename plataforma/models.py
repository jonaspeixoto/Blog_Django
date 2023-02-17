from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    imagem_post = models.ImageField()
    resumo = models.TextField()
    conteudo = models.TextField()

    def __str__(self):
        return str(self.titulo)