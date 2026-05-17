from rest_framework import serializers
from .models import Consulta, Especialista
from .services import ConsultaService


class EspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialista
        fields = ['id', 'nome', 'especialidade']


class ConsultaSerializer(serializers.ModelSerializer):

    hora = serializers.TimeField(format='%H:%M')
    especialista_detalhes = EspecialistaSerializer(source='especialista', read_only=True)
    
    medico = serializers.CharField(write_only=True)
    especialidade = serializers.CharField(write_only=True)


    class Meta:
        model = Consulta
        fields = ['id', 'data', 'hora', 'localizacao', 'medico', 'especialidade', 'especialista_detalhes']
        extra_kwargs = {
            'data': {'required': True},
            'hora': {'required': True},
            'localizacao': {'required': True, 'allow_blank': False},
        }
        

    def validate(self, data):
        ConsultaService.validar_data_hora(
            data_consulta=data.get('data'),
            hora_consulta=data.get('hora')
        )
        return data

    def create(self, validated_data):
        nome_medico = validated_data.pop('medico')
        nome_especialidade = validated_data.pop('especialidade')

        especialista, created = Especialista.objects.get_or_create(
            nome__iexact=nome_medico,
            especialidade__iexact=nome_especialidade,
            defaults={'nome': nome_medico, 'especialidade': nome_especialidade}
        )

        consulta = Consulta.objects.create(especialista=especialista, **validated_data)
        return consulta
