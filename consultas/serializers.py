from rest_framework import serializers
from .models import Consulta, Especialista, HorarioDisponivel

class HorarioDisponivelSerializer(serializers.ModelSerializer):
    horario = serializers.TimeField(format="%H:%M")

    class Meta:
        model = HorarioDisponivel
        fields = ['id', 'horario', 'disponivel']


class EspecialistaSerializer(serializers.ModelSerializer):
    horarios_disponiveis = HorarioDisponivelSerializer(many=True, read_only=True)

    class Meta:
        model = Especialista
        fields = ['id', 'nome', 'especialidade', 'horarios_disponiveis']


class ConsultaSerializer(serializers.ModelSerializer):
    especialista_detalhes = EspecialistaSerializer(source='especialista', read_only=True)
    
    horario_texto = serializers.ReadOnlyField(source='horario_selecionado.horario')

    class Meta:
        model = Consulta
        fields = ['id', 'data', 'horario_selecionado', 'horario_texto', 'localizacao', 'especialista', 'especialista_detalhes']
        extra_kwargs = {
            'data': {'required': True},
            'horario_selecionado': {'required': True},
            'localizacao': {'required': True, 'allow_blank': False},
            'especialista': {'required': True},
        }
