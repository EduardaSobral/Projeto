from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Psicologo(User):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField(("Data de nascimento (ano-mês-dia)"))
    telefone = models.CharField(max_length=15)
    CRP = models.CharField(max_length=15)
    CPF = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.nome

