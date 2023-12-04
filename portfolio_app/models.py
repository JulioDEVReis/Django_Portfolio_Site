from django.db import models

class Projetos(models.Model):
    nome = models.CharField(max_length=200)
    subtitulo = models.TextField()
    imagem = models.ImageField(upload_to='static/assets/img')
    teconlogias = models.TextField()
    descricao = models.TextField()
    problemas_solucoes = models.TextField()
    