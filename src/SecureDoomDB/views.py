from django.shortcuts import render
from rest_framework import generics
from .serializers import IncidentsSerializer
from .serializers import CarsSerializer
from .models import InOutRegister
from .models import Incident
from django.db.models import Sum
# Create your views here.

class IncidentsView(generics.ListCreateAPIView):
    queryset = Incident.objects.all()#values('street__name').annotate(Sum('value'))
    serializer_class=IncidentsSerializer

    def perform_create(self,serializer):
        serializer.save()


class CarsView(generics.ListCreateAPIView):
    queryset = InOutRegister.objects.all()#values('street__name').annotate(Sum('value'))
    serializer_class=CarsSerializer

    def perform_create(self,serializer):
        serializer.save()
