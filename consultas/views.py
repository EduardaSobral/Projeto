from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from consultas.form import ConsultaForm, EditarConsultaForm

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

    print('Está aqui!')
    consultas = Consulta.objects.all()
    
    context = {
        'consultas': consultas,
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
    
    if request.method == "POST":
        form = EditarConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/consultas")
    else:    
        form = EditarConsultaForm(instance=consulta)
    
    context = {
        'form': form,
        'consulta_id': consulta_id
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
def myConsulta(request):

    return render(request, 'consultas/myConsulta.html', {})

