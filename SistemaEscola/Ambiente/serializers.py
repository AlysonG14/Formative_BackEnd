from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Ambiente, Professor, Disciplinar, Gestor, Reserva

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(read_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(
        queryset=Professor.objects.all(), source='professor', write_only=True
    )
    class Meta:
        model = Disciplinar
        fields = '__all__'

class AmbienteSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(read_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(
        queryset= Professor.objects.all(), source='professor', write_only=True
    )

    disciplina = DisciplinaSerializer(read_only=True)
    disciplina_id = serializers.PrimaryKeyRelatedField(
        queryset= Disciplinar.objects.all(), source='disciplina', write_only=True
    )

    class Meta:
        model = Ambiente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(read_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(
        queryset = Professor.objects.all(), source='professor', write_only=True
    )
    disciplina = DisciplinaSerializer(read_only=True)
    disciplina_id = serializers.PrimaryKeyRelatedField(
        queryset = Disciplinar.objects.all(), source='disciplina', write_only=True
    )

    ambiente = AmbienteSerializer(read_only=True)
    ambiente_id = serializers.PrimaryKeyRelatedField(
        queryset = Ambiente.objects.all(), source='ambiente', write_only=True
    )


    class Meta:
        model = Reserva
        fields = '__all__'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['sistema'] = user.sistema
        return token
    
class GestorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Gestor
        fields = ('email', 'username', 'password', 'nome', 'idade', 'foto', 'sistema')

    def create(self, validated_data):
        user = Gestor.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            nome=validated_data['nome'],
            idade=validated_data['idade'],
            foto=validated_data['foto'],
            sistema=validated_data['sistema']
    )
        return user

