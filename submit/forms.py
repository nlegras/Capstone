from django import forms
from django.forms.widgets import SelectDateWidget


class rideForm(forms.Form):
    departDate = forms.DateField()
    departTime = forms.TimeField()
    seatCapacity = forms.IntegerField()   
    departLocation = forms.CharField()
    arrivalLocation = forms.CharField() 
    driverEmail = forms.EmailField()
    riderPrice = forms.DecimalField(max_digits=5, decimal_places=2)
    drisSmokes = forms.CheckboxSelectMultiple()
    ridersPets = forms.CheckboxSelectMultiple()
    ridersLugg = forms.IntegerField()
    print('hello')
    


