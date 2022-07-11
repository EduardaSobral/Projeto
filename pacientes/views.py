
from django.shortcuts import render
from .form import PacienteForm
from .models import Paciente
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    print('Está aqui!')
    pacientes = Paciente.objects.all()

    context = {
        'pacientes': pacientes,
    }
    
    return render(request, 'pacientes/index.html', context)

@login_required
def detail(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    context = {
        'paciente': paciente
    }

    return render(request, 'pacientes/detail.html', context)

#método para excluir uma paciente
@login_required
def excluir(request, paciente_id):

    Paciente.objects.get(pk=paciente_id).delete()
    
    return HttpResponseRedirect("/pacientes")

#método para criar uma nova paciente
@login_required
def criar(request):

    if request.method == "POST":

        form = PacienteForm(request.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/pacientes")
    else:
        form = PacienteForm()

    context = {
        'form': form
    }

    return render(request, 'pacientes/criar.html', context)

#método para editar um registro de paciente
@login_required
def editar(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)

    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/pacientes")
    else:
        form = PacienteForm(instance=paciente)

    context = {
        'form': form,
        'paciente_id': paciente_id
    }

    return render(request, 'pacientes/editar.html', context)
