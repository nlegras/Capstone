from django.shortcuts import render
from django.http import HttpResponse
from .forms import rideForm
from .models import Rides
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = rideForm(request.POST)
        if form.is_valid():
            departDate  = request.POST.get('departDate')
            departTime  = request.POST.get('departTime')
            departCity  = request.POST.get('departCity')
            departState = request.POST.get('departState')
            departZip = request.POST.get('departZip')
            if not departZip:
                departZip = zcdb.find_zip(city=departCity, state=departState)[0].zip
            print("check: ", departZip)
            # departZip   = zcdb.find_zip(city=request.POST.get('departCity'), state=request.POST.get('departState'))[0].zip
            # print(departZip)
            arrivalZip  = request.POST.get('arrivalZip')
            # arrivalCity  = request.POST.get('aCity')
            # arrivalState = request.POST.get('aState')
            # arrivalZip   = zcdb.find_zip(city=arrivalCity, state=arrivalState)[0].zip          
            driverEmail = request.POST.get('driverEmail')
            rideLugg    = request.POST.get('ridersLugg')
            seatCapac   = request.POST.get('seatCapacity')
            riderPrice  = request.POST.get('riderPrice')
            if request.POST.get('drisSmokes') == 'on':
                driverSmokes = 1
            else:
                driverSmokes = 0
            if request.POST.get('ridersPets') == 'on':
                ridePets = 1
            else:
                ridePets = 0
            print(form)
            print(form.cleaned_data)
            record = Rides(depDate=departDate, depTime=departTime, depZip=departZip, arrZip=arrivalZip, driEmail=driverEmail, seatCapacity=seatCapac, reserved='Open', driSmokes=driverSmokes, riderPets=ridePets, riderLugg=rideLugg, riderPrice=riderPrice)
            print(record.depZip) 
            record.save()
        else:
            pass
            print(form.errors)
            
    return render(request, 'rideSubmit.html')
