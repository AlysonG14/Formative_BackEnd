from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Professor(models.Model):
    ni = models.IntegerField(null= True, blank= True)
    nome = models.CharField(max_length= 255, blank=True, null=True)
    email = models.CharField(max_length= 255, blank=True, null=True)
    telefone = models.CharField(max_length= 16, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                                         message='O número tem que ser o formato de: 19 12345-6789')], blank= True, null= True) 
    data_nascimento = models.DateField(blank=True, null=True)
    data_contratacao = models.DateField(blank=True, null=True)


    def __str__(self):
        return f'{self.ni}- {self.nome}'
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

CURSO = [
    ('MC', 'Mecatrônica'),
    ('ADM', 'Administração'),
    ('ADS', 'Análise e Desenvolvimento de Sistemas'),
    ('MA', 'Manufatura'),

]

class Disciplinar(models.Model):
    nome = models.CharField(max_length= 255, blank=True, null=True)
    curso = models.CharField(max_length= 3, choices=CURSO, blank=True, null=True)
    carga_horaria = models.DurationField(blank=True, null=True)
    descricao = models.CharField(max_length= 255, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

class Ambiente(models.Model):
    sala = models.CharField(max_length=255, blank=True, null=True)
    capacidade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return(self.sala)
    
    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'

PERIODO = [
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite')
]

class Reserva(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='reservas')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reservas')
    disciplina = models.ForeignKey(Disciplinar, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(blank=True, null=True)
    data_termino = models.DateTimeField(blank=True, null=True)
    periodo = models.CharField(max_length=5, choices=PERIODO, blank=True, null=True)

    def __str__(self):
        return f'{self.periodo}'
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

SISTEMAS = [
    ('P', 'Professores'),
    ('D', 'Disciplinas'),
    ('A', 'Ambientes')
]

class Gestor(AbstractUser):
    sistema = models.CharField(max_length=1, choices=SISTEMAS, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    idade = models.PositiveIntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to='images/', blank=True, null= True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email