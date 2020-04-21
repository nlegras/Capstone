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
            if request.POST.get('driSmokes') == 'on':
                driverSmokes = True
            else:
                driverSmokes = False
            if request.POST.get('riderPets') == 'on':
                ridePets = True
            else:
                ridePets = False
            rideLugg = request.POST.get('riderLugg')
            record = Rides(depDate=departDate, depTime=departTime, depZip=departZip, arrZip=arrivalZip, driEmail=driverEmail, reserved='Open', driSmokes=driverSmokes, riderPets=ridePets, riderLugg=rideLugg)
            record.save()
        else:
            pass
            
    return render(request, 'rideSubmit.html')
