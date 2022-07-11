from imp import new_module
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Cadastro
from consultas.form import ConsultaForm, EditarConsultaForm
from datetime import datetime, timedelta, time, date

from .models import Consulta

@login_required
def criar(request):

    if request.method == "POST": 
        form = ConsultaForm(request.POST)

        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/consultas")
    else: 
        form = ConsultaForm()

    context = {
        'form': form
    }

    return render(request, 'consultas/criar.html/', context)

@login_required
def index(request):
    is_Alunos = request.user.groups.filter(name='Alunos').exists()
    print('Está aqui!')
    consultas = Consulta.objects.filter(matricula='')
    
    context = {
        'consultas': consultas,
        'is_Alunos': is_Alunos
    }

    return render(request, 'consultas/index.html', context)

#método para detalhar consultas
@login_required
def detail(request, consulta_id):
    consulta = Consulta.objects.get(pk=consulta_id)
    context = {
        'consulta': consulta
    }

    return render(request, 'consultas/detail.html', context)

@login_required
def editar(request, consulta_id):
    consulta = Consulta.objects.get(pk=consulta_id)

    is_Alunos = request.user.groups.filter(name='Alunos').exists()
    form  = ""
    if request.method == "POST":
        if is_Alunos:
            form.instance.matricula= request.user.id
            form = EditarConsultaForm(request.POST, instance=consulta)
        else:
            form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/consultas")
    else:    
        if is_Alunos:
            form = EditarConsultaForm(instance=consulta)
        else:
            form = ConsultaForm(instance=consulta)
    
    context = {
        'form': form,
        'consulta_id': consulta_id,
        'is_Alunos': is_Alunos
    }
    
    return render(request, 'consultas/editar.html', context)

@login_required
def editarPsi(request, consulta_id):
    consulta = Consulta.objects.get(pk=consulta_id)
    
    if request.method == "POST":
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/consultas")
    else:    
        form = ConsultaForm(instance=consulta)
    
    context = {
        'form': form,
        'consulta_id': consulta_id
    }
    
    return render(request, 'consultas/editar.html', context) 

@login_required
def excluir(request, consulta_id):
    
    Consulta.objects.get(pk=consulta_id).delete()
    
    return HttpResponseRedirect("/consultas")

@login_required
def excluirM(request, consulta_id):

    Consulta.objects.get(pk=consulta_id).delete()

    
    
    return HttpResponseRedirect("/consultas/myConsulta")

@login_required
def myConsulta(request):
    is_Alunos = request.user.groups.filter(name='Alunos').exists()
    Idmatricula = Consulta.objects
    if is_Alunos:
        #colocar a consulta da matricula do aluno
        consultas = Consulta.objects.filter(matricula = Idmatricula)
    else:
        today = datetime.today().date()
        consultas = Consulta.objects.filter(data__date=today)
        consultas = Consulta.objects.filter(matricula__contains = '2')
    
    context = {
        'consultas': consultas,
        'is_Alunos': is_Alunos
    }

    return render(request, 'consultas/myConsulta.html', context)


