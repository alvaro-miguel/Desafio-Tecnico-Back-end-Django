from django.db import models


class Especialista(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=50)


    class Meta:
        db_table = 'especialistas'
        verbose_name = 'Especialista'
        verbose_name_plural = 'Especialistas'
        ordering = ['nome']


    def __str__(self):
        return f"{self.nome} - {self.especialidade}"


class Consulta(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    localizacao = models.CharField(max_length=50)
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE, related_name='consultas')


    class Meta:
        db_table = 'consultas'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['data', 'hora']


    def __str__(self):
        return f"{self.especialista} - {self.data} às {self.hora}"
