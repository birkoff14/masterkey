from django import forms
from .models import Tickets, TipoSoporte
from django.contrib.auth.models import User

class TicketsForm(forms.ModelForm):

    class Meta:
        model = Tickets
        fields = ["idUsuario", "idTipo", "descripcion"]

    usuarios = (
        ('1', 'Manuel'),
        ('2', 'David'),
        ('3', 'Axcel'),
        ('4', 'Ricardo'),
        ('5', 'Yampool'),
    )
    idUsuario = forms.ModelChoiceField(label="Usuario", queryset=User.objects.all())
    idTipo = forms.ModelChoiceField(label="Tipo", queryset=TipoSoporte.objects.all())
    descripcion = forms.CharField(label='Descripción', widget = forms.Textarea)