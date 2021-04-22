from .serializers import TicketsSerializer
from .models import Tickets
from rest_framework import generics


class TicketsList(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class TicketsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer