from django.db import models

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
    idTicket = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    idUsuario = models.CharField(max_length=2)
    #tipo = models.CharField(max_length=2)
    idTipo = models.ForeignKey(TipoSoporte, on_delete=models.CASCADE, null=True)
    descripcion = models.CharField(max_length=1000)