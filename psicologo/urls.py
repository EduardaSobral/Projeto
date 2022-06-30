from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='Register'),
    path('password/', views.password, name='Password')
]