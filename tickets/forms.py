from django import forms
from .models import Tickets, TipoSoporte

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
    idUsuario = forms.ChoiceField(label='Usuario', widget=forms.Select, choices=usuarios)
    idTipo = forms.ModelChoiceField(queryset=TipoSoporte.objects.all())
    descripcion = forms.CharField(label='Descripción', widget = forms.Textarea)