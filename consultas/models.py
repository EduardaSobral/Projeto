from django.db import models

class Consulta(models.Model):
    CRP = models.CharField(max_length=15)
    matricula= models.CharField(max_length=15, null=False, blank=True)
    data = models.DateTimeField("Data da consulta (00/00/0000   00:00)")
    horario = models.TimeField("Horário da consulta")

    def __str__(self):
        return self.data