from django.db import models
from datetime import datetime

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=50)
    passing_year = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name