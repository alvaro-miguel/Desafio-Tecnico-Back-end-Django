from django.contrib import admin
from .models import Especialista, HorarioDisponivel, Consulta

admin.site.register(Especialista)
admin.site.register(HorarioDisponivel)
admin.site.register(Consulta)