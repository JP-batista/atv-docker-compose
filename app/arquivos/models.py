import os

from django.db import models


class Arquivo(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to="uploads/%Y/%m/%d/")
    enviado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-enviado_em"]

    def __str__(self):
        return self.titulo

    @property
    def nome(self):
        return os.path.basename(self.arquivo.name)
