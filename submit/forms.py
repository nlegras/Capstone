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
    arrivalCity = forms.CharField(required=False)
    arrivalState = forms.CharField(required=False)  
    arrivalZip = forms.CharField(required=False)
    driverEmail = forms.EmailField()
    riderPrice = forms.DecimalField(max_digits=5, decimal_places=2)
    drisSmokes = forms.CheckboxSelectMultiple()
    ridersPets = forms.CheckboxSelectMultiple()
    ridersLugg = forms.IntegerField()
    print('hello')
    
    def clean_departZip(self):
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
        
    def clean_arrivalZip(self):
        cleaned_data = super().clean()
        arrivalCity = cleaned_data.get('arrivalCity')
        arrivalState = cleaned_data.get('arrivalState')
        arrivalZip = cleaned_data.get('arrivalZip')
        
        if not arrivalZip:
            if arrivalCity and arrivalState:
                arrivalZip = zcdb.find_zip(city=arrivalCity, state=arrivalState)[0].zip
            else:
                if not arrivalCity:
                    self.add_error('arrivalCity', 'no city')
                if not arrivalState:
                    self.add_error('arrivalState', 'no state')
        return self.cleaned_data

