from .models import Paciente
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class PacienteForm(ModelForm): 

    class Meta:
        model = Paciente
        fields =(
        'nome',
        'texto'
        )

