from django.db import models
from django.conf import settings
from django.utils import timezone
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()
# Create your models here.

class Rides(models.Model):
    depDate = models.DateField()
    depTime = models.TimeField()
    depZip = models.IntegerField()
    arrZip = models.IntegerField()
    driEmail = models.EmailField()
    reserved = models.TextField(default='Open')
    driSmokes = models.IntegerField(default=0)
    riderPets = models.IntegerField(default=0)
    riderLugg = models.IntegerField(default=0)
    
    def __str__(self):
        return self.depDate
        
    @property
    def depName(self):
        return zcdb[self.depZip].city + ", " + zcdb[self.depZip].state
    @property
    def arrName(self):
        return zcdb[self.arrZip].city + ", " + zcdb[self.arrZip].state        
    