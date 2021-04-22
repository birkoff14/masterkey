from .models import Tickets
from rest_framework import serializers

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('idUsuario', 'idTipo', 'descripcion', 'timestamp')