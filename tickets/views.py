from django.shortcuts import render, redirect
from .models import Tickets, TipoSoporte
from .forms import TicketsForm

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

# Create your views here.

def inicio(request):
    titulo = "Tickets de hoy"
    
    queryset = Tickets.objects.all()
    total = Tickets.objects.count()
    tAmb = Tickets.objects.filter(idTipo=1).count()

    context = {
        "titulo" : titulo,
        "qry" : queryset,
        "total" : total,
        "tAmb" : tAmb
    }

    print(queryset)

    return render(request, "inicio.html", context)

def tickets(request):
    if request.user.is_authenticated:
        titulo = "Registra tu ticket"

        form = TicketsForm(request.POST or None)     

        if form.is_valid():
            formulario = form.save(commit=False)
            idUsuario = form.cleaned_data.get("idUsuario")
            idTipo = form.cleaned_data.get("idTipo")
            #idTipo = TipoSoporte.objects.get(idTipo = form.cleaned_data.get("idTipo"))
            desc = form.cleaned_data.get("descripcion")
            formulario.save()

            #print(formulario)
            #print(formulario.timestamp)

        context = {
            "titulo" : titulo,
            "frm" : form
        }
        
        return render(request, "addTicket.html", context)

    return redirect('/login')

def menu(request):
    titulo = "Menú principal"

    context = {
        "titulo" : titulo
    }

    if request.user.is_authenticated:
        return render(request, "menu.html", context)
    return redirect('/login')

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:                
                do_login(request, user)
                return redirect('/menu')
    return render(request, "login.html", {'form' : form})

def logout(request):
    do_logout(request)
    return redirect('/')

def registro(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()

            if user is not None:
                do_login(request, user)
                return redirect("/menu")
    return render(request, "register.html", {"form" : form})