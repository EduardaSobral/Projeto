from django.urls import path

from . import views

urlpatterns = [
    path('criar/', views.criar, name='criar'),
    path('', views.index, name='index'),
    path('<int:consulta_id>/', views.detail, name='detail'),
    path('editar/<int:consulta_id>/', views.editar, name='editar'),
    path('editarPsi/<int:consulta_id>/', views.editarPsi, name='editarPsicologo'),
    path('excluir/<int:consulta_id>/', views.excluir, name='excluir'),
    path('excluirM/<int:consulta_id>/', views.excluirM, name='excluir minha consulta'),
    path('myConsulta/', views.myConsulta, name='myConsulta'),
]
