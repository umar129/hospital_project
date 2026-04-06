from django.db import models
from doctors.models import Doctors

# Create your models here.

class Patients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    address = models.TextField()
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=128)
    doctor = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

