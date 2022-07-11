from django.urls import path

from . import views

urlpatterns = [
    path('registerPsico/', views.register, name='Register'),
    path('passwordPsico/', views.password, name='Password'),
    path('detail/', views.Psicologo, name='detail'),

]