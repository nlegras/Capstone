from django import forms

class rideForm(forms.Form):
    departDate = forms.DateField()
    departTime = forms.TimeField()
    seatCapacity = forms.IntegerField()
    departZip = forms.IntegerField()
    arrivalZip = forms.IntegerField()
    driverEmail = forms.EmailField()
    riderPrice = forms.DecimalField(max_digits=5, decimal_places=2)
    drisSmokes = forms.CheckboxSelectMultiple()
    ridersPets = forms.CheckboxSelectMultiple()
    ridersLugg = forms.IntegerField()
