from django.db import migrations
from datetime import time

def popular_dados_iniciais(apps, schema_editor):
    Especialista = apps.get_model('consultas', 'Especialista')
    HorarioDisponivel = apps.get_model('consultas', 'HorarioDisponivel')

    dr_fernando = Especialista.objects.create(nome="Dr. Fernando Miguel", especialidade="Cardiologia")
    dr_joao = Especialista.objects.create(nome="Dr. Joao de Souza", especialidade="Pediatria")
    dr_lucas = Especialista.objects.create(nome="Dr. Lucas Lima", especialidade="Ortopedia")
    dra_maria = Especialista.objects.create(nome="Dr. Maria Conceicao", especialidade="Ortopedia")
    dra_joana = Especialista.objects.create(nome="Dr. Joaoa da Silva", especialidade="Ortopedia")
    dr_bruno = Especialista.objects.create(nome="Dr. Bruno Costa", especialidade="Ortopedia")
    dra_bruna = Especialista.objects.create(nome="Dr. Bruna Carvalho", especialidade="Ortopedia")
    dr_luis = Especialista.objects.create(nome="Dr. Luis Gomes", especialidade="Ortopedia")

    horarios_padrao = [time(8, 0), time(9, 0), time(10, 0), time(14, 0), time(15, 0)]

    for h in horarios_padrao:
        HorarioDisponivel.objects.create(especialista=dr_fernando, horario=h, disponivel=True)
        HorarioDisponivel.objects.create(especialista=dr_joao, horario=h, disponivel=True)
        HorarioDisponivel.objects.create(especialista=dr_lucas, horario=h, disponivel=True)
        HorarioDisponivel.objects.create(especialista=dra_maria, horario=h, disponivel=True)
        HorarioDisponivel.objects.create(especialista=dra_joana, horario=h, disponivel=True)
        HorarioDisponivel.objects.create(especialista=dr_bruno, horario=h, disponivel=True)
        HorarioDisponivel.objects.create(especialista=dra_bruna, horario=h, disponivel=True)
        HorarioDisponivel.objects.create(especialista=dr_luis, horario=h, disponivel=True)

class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_alter_consulta_options_remove_consulta_hora_and_more'),
    ]

    operations = [
        migrations.RunPython(popular_dados_iniciais),
    ]