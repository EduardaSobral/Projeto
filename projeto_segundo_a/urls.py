from django import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('home.urls')),
    path('consultas/', include('consultas.urls')),
    path('psicologo/', include('psicologo.urls')),
    path('pacientes/', include('pacientes.urls'))
]
