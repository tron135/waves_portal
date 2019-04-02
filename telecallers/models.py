from django.db import models
from datetime import datetime

# Create your models here.
class Telecaller(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    dob = models.DateTimeField()
    sscname = models.CharField(max_length=128, blank=True)
    sscpassyr = models.IntegerField(blank=True)
    hscname = models.CharField(max_length=256,blank=True)
    hscpassyr = models.IntegerField(blank=True)
    diplname = models.CharField(max_length=256,blank=True)
    diplpassyr = models.IntegerField(blank=True)
    degname = models.CharField(max_length=256,blank=True)
    degpassyr = models.IntegerField(blank=True)
    masname = models.CharField(max_length=256,blank=True)
    maspassyr = models.IntegerField(blank=True)
    designation = models.CharField(max_length=128)
    passyr = models.IntegerField()
    expyr = models.IntegerField()
    expmon = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)