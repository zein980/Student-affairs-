from django.db import models
# Create your models here.


class Student (models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    idst = models.CharField(max_length=10)
    department = models.CharField(max_length=60)
    level = models.IntegerField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateField()
    gender = models.CharField(max_length=10)
    status = models.BooleanField(default=True)


