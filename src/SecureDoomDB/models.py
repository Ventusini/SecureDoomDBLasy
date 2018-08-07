from django.db import models
import datetime
# Create your models here.
class Street(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)

    def __str__(self):
        return self.name
        
    def __unicode__(self):
        return self.name

class House(models.Model):
    private_street = models.ForeignKey(Street, on_delete=models.CASCADE)
    

class Resident(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name

class Car(models.Model):
    propietary = models.ForeignKey(Resident, on_delete=models.CASCADE)
    plates = models.CharField(max_length=30, blank=False, unique=True)
    model = models.CharField(max_length=30, blank=False)
    isIn = isIn = models.BooleanField(default=True)
    def __str__(self):
        return self.plates

class InOutRegister(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.date.today)
    kind =  models.CharField(max_length=3, blank=False)
    def __str__(self):
        return self.kind

class Sensor(models.Model):
    type=models.CharField(max_length=30, blank=False)

class Incident(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    street = models.ForeignKey(Street, related_name='street_name', on_delete=models.CASCADE, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.date.today)
    type = models.CharField(max_length=30, default="False Alarm")