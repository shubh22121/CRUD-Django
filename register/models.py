from django.db import models

# Create your models here.



class position (models.Model):
    title = models.CharField(max_length=50)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    phone = models.CharField(max_length=15)
    position = models.ForeignKey(position, on_delete=models.CASCADE)
    