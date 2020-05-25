from django.db import models

class Departamentos (models.Model):
    departamentos = models.CharField(max_length=50)