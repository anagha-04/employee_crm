from django.db import models

# Create your models here.

class Employeemodel(models.Model):

    name = models.CharField(max_length=20)

    role = models.CharField(max_length=20)

    place = models.CharField(max_length=20)

    salary = models.IntegerField()
    
