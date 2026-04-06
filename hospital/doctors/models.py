from django.db import models

# Create your models here.

class Departments(models.Model):
    DEPARTMENT_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Dermatology', 'Dermatology'),
        ('General', 'General'),
    ]
    
    id = models.AutoField(primary_key=True)
    dep_name = models.CharField(max_length=128, choices=DEPARTMENT_CHOICES, unique=True)
    
    def __str__(self):
        return self.dep_name
    
    class Meta:
        verbose_name_plural = "Departments"


class Doctors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True, blank=True)
    joining_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    salary = models.IntegerField()
