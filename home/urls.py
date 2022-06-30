from django.urls import path

from . import views

urlpatterns = [
    
    path('template/', views.template, name="template"),
    path('informacao', views.informacao, name="informacao"),
    path('informacao2', views.informacao2, name="informacao2"),
    path('inicio/', views.inicio, name="inicio"),
    path('redireciona/', views.redireciona, name="redireciona")
]