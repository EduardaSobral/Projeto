from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:paciente_id>/', views.detail, name='detail'),
    path('excluir/<int:paciente_id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:paciente_id>/', views.editar, name='editar'),
]


