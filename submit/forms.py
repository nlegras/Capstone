from django import forms
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()



class rideForm(forms.Form):
    departDate = forms.DateField()
    departTime = forms.TimeField()
    seatCapacity = forms.IntegerField()
    departCity = forms.CharField(required=False)
    departState = forms.CharField(required=False)    
    departZip = forms.CharField(required=False)
    arrivalZip = forms.CharField()
    driverEmail = forms.EmailField()
    riderPrice = forms.DecimalField(max_digits=5, decimal_places=2)
    drisSmokes = forms.CheckboxSelectMultiple()
    ridersPets = forms.CheckboxSelectMultiple()
    ridersLugg = forms.IntegerField()
    print('hello')
    
    def clean(self):
        departCity = self.cleaned_data.get('departCity')
        departState = self.cleaned_data.get('departState')
        departZip   = zcdb.find_zip(city=departCity, state=departState)[0].zip
        print(departZip)
        if not (departCity and departState) and not departZip:
            raise forms.ValidationError('Enter city and state or zip')
        return self.cleaned_data

