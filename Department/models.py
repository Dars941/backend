from django.db import models

class Department(models.Model):
    department = models.CharField(max_length=255)
    hod = models.CharField(max_length=255)
