from django.db import models

# Create your models here.

class section(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    roll = models.IntegerField()
    score = models.IntegerField()