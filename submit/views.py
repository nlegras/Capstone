from django.shortcuts import render
from django.http import HttpResponse
from .forms import rideForm
from .models import Rides
from pyzipcode import ZipCodeDatabase
from django.contrib import messages
from address import AddressParser, Address
zcdb = ZipCodeDatabase()

# Create your views here.


def index(request):
    ap = AddressParser()
    if request.method == 'POST':
        form = rideForm(request.POST)
        if form.is_valid():
            departDate  = request.POST.get('departDate')
            departTime  = request.POST.get('departTime')
            departLocation = request.POST.get('departLocation')
            departLocation = ap.parse_address(departLocation)
            if not departLocation.zip:
                departZip = zcdb.find_zip(city=departLocation.city, state=departLocation.state)[0].zip
            else:
                departZip = departLocation.zip
            arrivalLocation = request.POST.get('arrivalLocation')
            arrivalLocation = ap.parse_address(arrivalLocation)
            if not arrivalLocation.zip:
                arrivalZip = zcdb.find_zip(city=arrivalLocation.city, state=arrivalLocation.state)[0].zip
            else:    
                arrivalZip = arrivalLocation.zip
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
            record = Rides(depDate=departDate, depTime=departTime, depZip=departZip, arrZip=arrivalZip, driEmail=driverEmail, seatCapacity=seatCapac, reserved='Open', driSmokes=driverSmokes, riderPets=ridePets, riderLugg=rideLugg, riderPrice=riderPrice)
            record.save()
            messages.success(request, 'The Ride Offer was submitted successfully.')
        else:
            pass
            print(form.errors)
            
    return render(request, 'rideSubmit.html')
