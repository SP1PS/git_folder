# models.py
from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    email = models.EmailField(null=True)

    def __str__(self):  # Corrected indentation of __str__ method
        return self.name
