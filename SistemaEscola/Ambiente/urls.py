from django.contrib import admin
from django.urls import path
from . import views
from .views import CustomTokenObtainPairView, CustomTokenRefreshView, RegisterView, ProtectedView

urlpatterns = [
    path('', views.OverviewAPI, name='Ambientes'),
    path('professor/', views.ProfessorListView.as_view()),
    path('professor/create/', views.professor_create),
    path('professor/acesso/<int:pk>/', views.professor_detail),
    path('disciplina/', views.DisciplinaListView.as_view()),
    path('disciplina/create', views.createDisciplina),
    path('disciplina/acesso/<int:pk>', views.disciplina_detail),
    path('ambiente/', views.AmbienteListView.as_view()),
    path('ambiente/create', views.createAmbiente),
    path('ambiente/acesso/<int:pk>', views.detail_ambiente),
    path('reserva/', views.AmbienteListView.as_view()),
    path('reserva/create', views.createReserva),
    path('reserva/acesso/<int:pk>', views.detail_reserva),
    path('api/token', CustomTokenObtainPairView.as_view(), name='token_obtan_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/protected/', ProtectedView.as_view(), name='protected'),
]