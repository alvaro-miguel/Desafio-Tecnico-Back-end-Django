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
    

class HorarioDisponivel(models.Model):
    especialista = models.ForeignKey(
        Especialista,
        on_delete=models.CASCADE,
        related_name='horarios_disponiveis'
    )
    horario = models.TimeField()
    disponivel = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.especialista.nome} | {self.horario.strftime('%H:%M')}"


class Consulta(models.Model):
    data = models.DateField()
    horario_selecionado = models.ForeignKey(
        HorarioDisponivel,
        on_delete=models.CASCADE,
        related_name='consultas_agendadas'
    )
    localizacao = models.CharField(max_length=50)
    especialista = models.ForeignKey(
        Especialista, 
        on_delete=models.CASCADE, 
        related_name='consultas')


    class Meta:
        db_table = 'consultas'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['data', 'horario_selecionado']


    def __str__(self):
        hora_formatada = self.horario_selecionado.horario.strftime('%H:%M')
        return f"Consulta com {self.especialista.nome} em {self.data} às {hora_formatada}"
