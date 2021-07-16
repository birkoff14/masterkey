from django import forms
from .models import Tickets, TipoSoporte
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField, CKEditorWidget
 
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
    #idUsuario = forms.ModelChoiceField(label="Usuario", queryset=User.objects.all().values_list('id','first_name'))
    idUsuario = forms.ModelChoiceField(label="Usuario", queryset=User.objects.all())    
    idTipo = forms.ModelChoiceField(label="Tipo", queryset=TipoSoporte.objects.all())
    #descripcion = forms.CharField(label='Descripción', widget = forms.Textarea)
    descripcion = forms.CharField(label='Descripción', widget = CKEditorWidget(config_name='awesome_ckeditor'))
    #descripcion = RichTextField(config_name='awesome_ckeditor')    