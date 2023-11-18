from django.db import models

# Create your models here.

class Carlist(models.Model):
    name = models.CharField(max_length=50, null= False, blank = False )
    description = models.TextField()
    active = models.BooleanField(default = False)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)