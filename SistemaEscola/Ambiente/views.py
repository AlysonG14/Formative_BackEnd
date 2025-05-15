from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from .mypaginations import (MyPageNumberPaginationProfessor,
                            MyPageNumberPaginationDisciplinar,
                            MyPageNumberPaginationAmbiente,
                            MyPageNumberPaginationReserva)
from .models import Professor, Disciplinar, Ambiente, Reserva
from .serializers import (AmbienteSerializer,
                          ProfessorSerializer,
                          DisciplinaSerializer,
                          CustomTokenObtainPairSerializer,
                          GestorSerializer,
                          ReservaSerializer)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .permissions import (IsGestor,
                          IsDisciplina,
                          IsAmbiente,
                          )

# Create your views here.

@api_view(['GET'])
def OverviewAPI(request):
    api_urls = {
        "all_itens": '/',
        "Gerenciamento": '/admin/',
        "Professor": '/professor/',
        "Cadastro de Professor": '/professor/acesso/create/',
        "Detalhes de Professor": '/professor/acesso/<int:pk>/',
        "Disciplina": '/disciplina/',
        "Cadastro de Disciplina": '/disciplina/acesso/create/',
        "Detalhes de Disciplina": '/disciplina/acesso/<int:pk>/',
        "Ambiente": '/ambiente/',
        "Cadastro de Ambiente": '/ambiente/acesso/create/',
        "Detalhes de Ambiente": "/ambiente/acesso/<int:pk>/",
        'Reserva': '/reserva/',
        "Cadastro de Reserva": '/reserva/acesso/create/',
        "Detalhes de Reserva": '/reserva/acesso/<int:pk>'
    }
    return Response(api_urls)

class ProfessorListView(ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    pagination_class = MyPageNumberPaginationProfessor
    permission_classes = [IsAuthenticated, IsGestor]

@api_view(['POST'])
def professor_create(request):
    serializer = ProfessorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def professor_detail(request, pk):
    professor = get_object_or_404(Professor, pk=pk)

    if request.method == 'GET':
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ProfessorSerializer(professor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DisciplinaListView(ListAPIView):
    queryset = Disciplinar.objects.all()
    serializer_class = DisciplinaSerializer
    pagination_class = MyPageNumberPaginationDisciplinar
    permission_classes = [IsAuthenticated, IsDisciplina]

@api_view(['POST'])
def createDisciplina(request):
    serializer = DisciplinaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def disciplina_detail(request, pk):
    disciplina = get_object_or_404(Disciplinar, pk=pk)

    if request.method == 'GET':
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = DisciplinaSerializer(disciplina, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AmbienteListView(ListAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    pagination_class = MyPageNumberPaginationAmbiente
    permission_classes = [IsAuthenticated, IsAmbiente]


@api_view(['POST'])
def createAmbiente(request):
    serializer = AmbienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def detail_ambiente(request, pk):
    ambiente = get_object_or_404(Ambiente, pk=pk)

    if request.method == 'GET':
        serializer = AmbienteSerializer(ambiente)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        ambiente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReservaListView(ListAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    pagination_class = MyPageNumberPaginationReserva
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
def createReserva(request):
    serializer = ReservaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def detail_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.method == 'GET':
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = ReservaSerializer(reserva, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'DELETE':
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    pass

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = GestorSerializer(data=request.data)
        if serializer.is_valid():
            gestor = serializer.save()
            if gestor:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This view is protected"})
    
class ReservaProfessorList(ListAPIView):
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reserva.objects.filter(professor__user=user)
    
class ReservaDisciplinaList(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Disciplinar.objects.filter(professor__user=user)

