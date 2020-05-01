from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from submit.models import Rides
from django.utils import timezone
from .forms import reserveForm
# Create your views here.

def post_rides(request):
   rides = Rides.objects.filter(depDate__gte=timezone.now()).order_by('depDate','depTime')
   return render(request, 'rides.html', {'rides': rides})

def resRide(request):
   if request.method == "POST":
      resForm = reserveForm(request.POST)
      if resForm.is_valid():
         reserveID = request.POST.get('reserveID')
         reservation = Rides.objects.get(id=reserveID)
         reservation.seatTaken = reservation.seatTaken + 1
         reservation.save()

   return HttpResponseRedirect('.')

