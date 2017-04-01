from django.db import models

# Create your models here.


class Poo(models.Model):
    uuid = models.CharField(max_length=5)


class Measure(models.Model):
    poo = models.ForeignKey(Poo, on_delete=models.CASCADE)
    timestamp = models.FloatField()
    sensor_fr = models.FloatField()
    sensor_fl = models.FloatField()
    sensor_br = models.FloatField()
    sensor_bl = models.FloatField()
