# models.py
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
