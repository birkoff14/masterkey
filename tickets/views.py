from django.shortcuts import render, redirect
from .models import Tickets, TipoSoporte
from .forms import TicketsForm
from django.db.models import Sum

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User

from django.db.models import Count

import sweetify

# Create your views here.

def inicio(request):
    titulo = "Tickets de hoy"
    
    #usuario = User.objects.all()
    queryset = Tickets.objects.all()
    total = Tickets.objects.count()
    tAmb = Tickets.objects.filter(idTipo=1).count()
    tImp = Tickets.objects.filter(idTipo=2).count()
    tTel = Tickets.objects.filter(idTipo=3).count()
    tSop = Tickets.objects.filter(idTipo=4).count()
    tDat = Tickets.objects.filter(idTipo=5).count()    
    
    context = {
        "titulo" : titulo,
        "qry" : queryset,
        "total" : total,
        "tAmb" : tAmb,
        "tImp" : tImp,
        "tTel" : tTel,
        "tSop" : tSop,
        "tDat" : tDat,
    }

    print(queryset.query)

    return render(request, "inicio.html", context)

def tickets(request):
    if request.user.is_authenticated:
        titulo = "Registra tu ticket"

        form = TicketsForm(request.POST or None)

        if form.is_valid():
            print("Si entra")
            formulario = form.save(commit=False)
            idUsuario = form.cleaned_data.get("idUsuario")
            idTipo = form.cleaned_data.get("idTipo")            
            desc = form.cleaned_data.get("descripcion")
            formulario.save()
            
            sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
            return redirect('mytickets')

        context = {
            "titulo" : titulo,
            "frm" : form
        }
        
        return render(request, "addTicket.html", context)
        

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
                #do_login(request, user)
                return redirect("/menu")

    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    
    return render(request, "register.html", {"form" : form})

def myTickets(request):
    titulo = "Mis tickets"
    user = request.user   

    #print("Mi user id es:",  user.id)

    queryset = Tickets.objects.filter(idUsuario=user)
    total = Tickets.objects.filter(idUsuario=user).count()
    tAmb = Tickets.objects.filter(idTipo=1, idUsuario=user).count()
    tImp = Tickets.objects.filter(idTipo=2, idUsuario=user).count()
    tTel = Tickets.objects.filter(idTipo=3, idUsuario=user).count()
    tSop = Tickets.objects.filter(idTipo=4, idUsuario=user).count()
    tDat = Tickets.objects.filter(idTipo=5, idUsuario=user).count()

    context = {
        "titulo" : titulo,
        "qry" : queryset,
        "total" : total,
        "tAmb" : tAmb,
        "tImp" : tImp,
        "tTel" : tTel,
        "tSop" : tSop,
        "tDat" : tDat,
        "usr" : user,
    }

    return render(request, "myTickets.html", context)

def ticketModal(request, pk):
    
    titulo = "Detalle del ticket"
    query = Tickets.objects.get(idTicket=pk)
    
    #print(query)
    
    context = {
        "titulo" : titulo,
        "query" : query,
    }
    
    return render(request, "modal.html", context)
    
def test_view(request):
    x = sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
    print(x)
    return redirect('/')    
    
def stadistics(request):
    titulo = "Estadísticas"
    
    
    qry = Tickets.objects.raw("select 1 as id, month(timestamp) Mes, year(timestamp) Año, b.descripcion, "
                              "count(1) Total "
                              "FROM  tickets_tickets tt "
                              "inner join tickets_tiposoporte b "
                              "on tt.idTipo_id = b.idTipo "
                              "where 1=1 and date(tt.timestamp) between '2020-11-01' and date(now()) "
                              "group by month(timestamp), year(timestamp)")
    
    #qry = Tickets.objects.raw("select 1 Mes, 1 Año, 1 descripcion, ")
        
    print(qry.query)
    
    context = {
        "titulo" : titulo,
        "rpt" : qry,
    }
    
    return render(request, "stadistics.html", context)