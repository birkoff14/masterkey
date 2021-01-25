from django.contrib import admin
from .models import Tickets, TipoSoporte

# Register your models here.
#admin.site.register(Tickets)
admin.site.register(TipoSoporte)

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('idTicket', 'timestamp', 'idUsuario', 'idTipo')
    
