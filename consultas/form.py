from .models import Consulta

from django.forms import ModelForm

#formulario para o psicologo
class ConsultaForm(ModelForm): 

    class Meta:
        model = Consulta
        fields = (
            'CRP',
            'data',
            'matricula'
        )

#formulario para o Aluno
class EditarConsultaForm(ModelForm): 

    def __init__(self, *args, **kwargs):
       super(EditarConsultaForm, self).__init__(*args, **kwargs)
       self.fields['CRP'].widget.attrs['readonly'] = True
       self.fields['data'].widget.attrs['readonly'] = True

    class Meta:
        model = Consulta
        fields = (
            'CRP',
            'data',
            'matricula'
        )