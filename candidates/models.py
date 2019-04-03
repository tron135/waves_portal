from django.db import models
from datetime import datetime

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=128)
    qualification = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    colname = models.CharField(max_length=256,blank=True)
    address = models.CharField(max_length=256)
    course = models.CharField(max_length=50)
    remark = models.CharField(max_length=512)
    reason = models.CharField(max_length=512)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name