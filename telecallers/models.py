from django.db import models
from datetime import datetime

# Create your models here.
class Telecaller(models.Model):
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=20)
    tele_phone = models.CharField(max_length=15)
    date = models.DateTimeField(default=datetime.now, blank=True)