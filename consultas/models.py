from django.db import models

class Consulta(models.Model):
    CRP = models.CharField(max_length=15)
    matricula= models.CharField(max_length=15, null=False, blank=True)
    data = models.DateField("Data da consulta")
    horario = models.TimeField("Horário da consulta")

    def __str__(self):
        return self.data