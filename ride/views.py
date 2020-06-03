from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from submit.models import Rides
from django.utils import timezone
from .forms import reserveForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from address import AddressParser, Address
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()
ap = AddressParser()
# Create your views here.

@login_required
def post_rides(request):
   print("post_rides")
   rides = Rides.objects.filter(depDate__gte=timezone.now()).order_by('depDate','depTime')
   return render(request, 'rides.html', {'rides': rides})

@login_required
def resRide(request):
   if request.method == "POST":
      resForm = reserveForm(request.POST)
      if resForm.is_valid():
         reserveID = request.POST.get('reserveID')
         reservation = Rides.objects.get(id=reserveID)
         reservation.seatTaken = reservation.seatTaken + 1

         #send email to driver
         driEmail = [reservation.driEmail]
         subject = 'Ride Offer Reserved'
         message = f'Someone accepted your ride on {reservation.depDate} from {reservation.depName} to {reservation.arrName} using EDUWheels!'
         email_from = settings.EMAIL_HOST_USER

         send_mail ( subject, message, email_from, driEmail )
         reservation.save()
         messages.success(request, 'The Ride Offer was reserved successfully.')


   return HttpResponseRedirect('.')

def rideDetails(request, id):
    ride = Rides.objects.get(id=id)
    context = {
        'ride': ride
    }
    return render(request, 'rideDetails.html', context)

def search(request):
   print("searching")

   results = Rides.objects.filter(depDate__gte=timezone.now()).order_by('depDate','depTime')
   depart = request.GET.get('depart')
   arrive = request.GET.get('arrive')
 
   if depart != '' and depart is not None:
      depart = ap.parse_address(depart)
      if not depart.zip:
         depart = zcdb.find_zip(city=depart.city, state=depart.state)[0].zip
      else:
         depart = depart.zip
      results = results.filter(depZip__icontains=depart)

   if arrive != '' and arrive is not None:
      arrive = ap.parse_address(arrive)
      if not arrive.zip:
         arrive = zcdb.find_zip(city=arrive.city, state=arrive.state)[0].zip
      else:    
         arrive = arrive.zip
      results = results.filter(arrZip__icontains=arrive)

   print(depart)
   print(arrive)

   return render(request, 'rides.html', {'rides': results})
