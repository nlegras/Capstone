from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class rides(models.Model):
    depDate = models.DateField()
    depTime = models.TimeField()
    depZip = models.IntegerField()
    arrZip = models.IntegerField()
    driEmail = models.EmailField()
    driSmokes = models.BooleanField()
    riderPets = models.BooleanField()
    riderLugg = models.IntegerField()
    
    def __str__(self):
        return self.depDate
        
    