from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def template(request):

    return render(request, '_base.html', {})

@login_required
def inicio(request):

    return render(request, 'home/inicio.html', {})

@login_required
def informacao(request):

    return render(request, 'home/informacao.html', {})

@login_required
def informacao2(request):

    return render(request, 'home/informacao2.html', {})

@login_required
def redireciona(request):
    
    if request.user.groups.filter(name='Alunos').exists():
        return HttpResponseRedirect('/home/inicio')
    else:
        return HttpResponseRedirect('/consultas/')
