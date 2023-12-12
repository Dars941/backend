from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    batch = models.CharField(max_length=10)
