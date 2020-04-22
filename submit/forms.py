from django import forms

class rideForm(forms.Form):
    departDate = forms.DateField()
    departTime = forms.TimeField()
    departZip = forms.IntegerField()
    arrivalZip = forms.IntegerField()
    driverEmail = forms.EmailField()
    drisSmokes = forms.CheckboxSelectMultiple()
    ridersPets = forms.CheckboxSelectMultiple()
    ridersLugg = forms.IntegerField()