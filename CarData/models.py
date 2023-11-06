from django.db import models

# Create your models here.

class Carlist(models.Model):
    name = models.CharField(max_length=50, null= False, blank = False )
    description = models.TextField()
    active = models.BooleanField(default = False)