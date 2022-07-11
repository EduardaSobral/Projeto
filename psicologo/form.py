from .models import Psicologo
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class PsicologoForm(UserCreationForm): 

    #método chamado para "limpar" os dados no momento que o 'form.is_valid()' é acionado no views.py
    def clean_password(self):
        return make_password(self.cleaned_data['password'])


    class Meta:
        model = Psicologo
        fields =(
        'nome',
        'data_nasc',
        'telefone',
        'CRP',
        'username',
        'email',
        'password1',
        'password2'
        )


    