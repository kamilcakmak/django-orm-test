from django.db import models
import datetime as dt
from django.core.validators import MaxValueValidator, MinValueValidator

# Q1 models
class Vehicle(models.Model):
    # models fields
    plate = models.CharField(max_length=10)

    def __str__(self):
        return self.plate

class Navigationrecord(models.Model):
    # models fields
    longitude = models.FloatField(validators=[MaxValueValidator(180), MinValueValidator(-180)])
    latitude = models.FloatField(validators=[MaxValueValidator(180), MinValueValidator(-180)]) 
    datetime = models.DateTimeField(default=dt.datetime.now)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    # model json serializer function
    def serialize(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'vehicle_plate': self.vehicle.plate,
            'datetime': self.datetime.strftime("%m.%d.%Y, %H:%M:%S")
        }

    class Meta:
        indexes = [
            models.Index(fields=['vehicle', 'datetime']),
        ]

# Q2

class Bin(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.FloatField(validators=[MaxValueValidator(180), MinValueValidator(-180)])
    latitude = models.FloatField(validators=[MaxValueValidator(180), MinValueValidator(-180)]) 

    def __str__(self):
        return self.name


class Operation1(models.Model):
    collection_frequency=models.IntegerField(default=1)
    last_collection = models.DateTimeField(default=dt.datetime.now)
    bin = models.OneToOneField(Bin, on_delete=models.CASCADE, related_name = "op1")

    def __str__(self):
        return self.bin.name

class Operation2(models.Model):
    collection_frequency=models.IntegerField(default=1)
    last_collection = models.DateTimeField(default=dt.datetime.now)
    bin = models.OneToOneField(Bin, on_delete=models.CASCADE, related_name = "op2")

    def __str__(self):
        return self.bin.name
