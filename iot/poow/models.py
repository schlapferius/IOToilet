from django.db import models

# Create your models here.

class PooSession(models.Model):
    uuid = models.CharField(max_length=5)
