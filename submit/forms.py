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
        cleaned_data = super().clean()
        departCity = cleaned_data.get('departCity')
        departState = cleaned_data.get('departState')
        departZip = cleaned_data.get('departZip')
        
        if not departZip:
            if departCity and departState:
                departZip = zcdb.find_zip(city=departCity, state=departState)[0].zip
            else:
                if not departCity:
                    self.add_error('departCity', 'no city')
                if not departState:
                    self.add_error('departState', 'no state')
        return self.cleaned_data

