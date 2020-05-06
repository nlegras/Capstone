from django.shortcuts import render
from django.http import HttpResponse
from .forms import rideForm
from .models import Rides
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = rideForm(request.POST)
        if form.is_valid():
            departDate = request.POST.get('departDate')
            departTime = request.POST.get('departTime')
            departZip = request.POST.get('departZip')
            arrivalZip = request.POST.get('arrivalZip')
            driverEmail = request.POST.get('driverEmail')
            rideLugg = request.POST.get('ridersLugg')
            seatCapac = request.POST.get('seatCapacity')
            riderPrice = request.POST.get('riderPrice')
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
        else:
            pass
            
    return render(request, 'rideSubmit.html')
