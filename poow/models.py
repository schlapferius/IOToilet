from django.db import models

# Create your models here.

class Poo(models.Model):
    uuid = models.CharField(max_length=5)
