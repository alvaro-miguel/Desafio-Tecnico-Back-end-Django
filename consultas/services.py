from django.utils import timezone
from rest_framework import serializers


class ConsultaService:
    @staticmethod
    def validar_data_hora(data_consulta, hora_consulta):
        data_hora_atual = timezone.now()

        if data_consulta < data_hora_atual.date():
            raise serializers.ValidationError({'data':'Data inválida'})
        
        if data_consulta == data_hora_atual.date():
            if hora_consulta < data_hora_atual.time():
                raise serializers.ValidationError({'hora':'Horá inválida'})
            
        return True