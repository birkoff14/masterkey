from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

#class Usuarios(models.Model):
#    idUsuario = models.AutoField(primary_key=True)
#    nombre = models.CharField(max_length=100, blank=True, null=True)
#    password = models.CharField(max_length=100, blank=True, null=True)
#    email = models.EmailField()
#    activo = models.DateTimeField(auto_now=False, auto_now_add=True)

class TipoSoporte(models.Model):
    idTipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion


class Tickets(models.Model):
    idTicket = models.AutoField(primary_key=True, verbose_name="Ticket")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Fecha")
    #timestamp = models.DateTimeField(default=timezone.now(), verbose_name="Fecha")
    #idUsuario = models.CharField(max_length=2, verbose_name="Usuario")
    idUsuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    #tipo = models.CharField(max_length=2)
    idTipo = models.ForeignKey(TipoSoporte, on_delete=models.CASCADE, null=True, verbose_name="Tipo")
    #descripcion = models.CharField(max_length=1000, verbose_name="Descripción")
    descripcion = RichTextField(blank=True, null=True, verbose_name="Descripción")