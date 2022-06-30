from django.shortcuts import render
from psicologo.form import PsicologoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

def register(request):
    
    if request.method == "POST":
        form = PsicologoForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)

            form.save()  

            form.save()            
            
            group = Group.objects.get(name='Psicologo')
            new_user.groups.add(group)

            # is_Psicologo = request.user.groups.filter(name='Psicologo').exists()

            return HttpResponseRedirect("/psicologo/login/")
    else:    
        form = PsicologoForm()
    
    context = {
        'form': form,
        # 'is_Psicologo' : is_Psicologo
    }
    
    return render(request, 'registration/register.html', context)

def password(request):
    
    if request.method == "POST":
        form = PsicologoForm(request.POST)
        if form.is_valid():
            
            form.save()            
            return HttpResponseRedirect("/psicologo/login/")
    else:    
        form = PsicologoForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'registration/forgot-password.html', context)

