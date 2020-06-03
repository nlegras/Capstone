from django.db import models
from django.conf import settings
from django.utils import timezone
from pyzipcode import ZipCodeDatabase
from datetime import datetime
zcdb = ZipCodeDatabase()
# Create your models here.

class Rides(models.Model):
    depDate = models.DateField()
    depTime = models.TimeField()
    depZip = models.CharField(max_length=50)
    arrZip = models.CharField(max_length=50)
    driEmail = models.EmailField()
    reserved = models.TextField(default='Open')
    seatTaken = models.IntegerField(default=0)
    seatCapacity = models.IntegerField(default=1)
    driSmokes = models.IntegerField(default=0)
    riderPets = models.IntegerField(default=0)
    riderLugg = models.IntegerField(default=0)
    riderPrice = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    
    @property
    def depName(self):
        return zcdb[self.depZip].city + ", " + zcdb[self.depZip].state
    @property
    def arrName(self):
        return zcdb[self.arrZip].city + ", " + zcdb[self.arrZip].state  
        
    def __str__(self):
        return self.depDate.strftime("%m/%d/%Y")+": "+self.depName+" to "+self.arrName
        
    @property
    def rPets(self):
        if (self.riderPets == 1):
            rPets = "Yes"
        elif (self.riderPets == 0):
            rPets = "No"
        return rPets
        
    @property
    def dSmokes(self):
        if (self.driSmokes == 1):
            dSmokes = "Yes"
        elif (self.driSmokes == 0):
            dSmokes = "No"
        return dSmokes
    