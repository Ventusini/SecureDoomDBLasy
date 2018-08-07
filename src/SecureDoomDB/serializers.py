from rest_framework import serializers
from .models import Incident
from .models import InOutRegister


class IncidentsSerializer(serializers.ModelSerializer):
    street_name = serializers.StringRelatedField(source='street', read_only=True)
    class Meta:
        model = Incident
        fields=('id', 'date', 'street_name', 'type')
        read_only_fields = ('id', 'date')     

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InOutRegister
        fields = ('id','time', 'car', 'kind')
        read_only_fields = ('id', 'time')
