from django.contrib import admin
from .models import Ambiente, Professor, Disciplinar, Reserva

# Register your models here.

@admin.register(Professor)
class AdminProfessor(admin.ModelAdmin):
    list_display = ['ni', 'nome', 'email', 'telefone']

@admin.register(Disciplinar)
class AdminDisciplinar(admin.ModelAdmin):
    list_display = ['nome', 'curso', 'carga_horaria', 'descricao', 'professor']

@admin.register(Ambiente)
class AdminAmbiente(admin.ModelAdmin):
    list_display = ['sala', 'capacidade']

@admin.register(Reserva)
class AdminReserva(admin.ModelAdmin):
    list_display = ['ambiente', 'professor', 'disciplina', 'data_inicio', 'data_termino', 'periodo']