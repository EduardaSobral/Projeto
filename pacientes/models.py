from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField("Observações")

    def __str__(self):
        return self.nome

