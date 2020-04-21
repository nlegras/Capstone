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
            record = Rides(depDate=departDate, depTime=departTime, depZip=departZip, arrZip=arrivalZip, driEmail=driverEmail, reserved='Open')
            record.save()
        else:
            pass
            
    return render(request, 'rideSubmit.html')
