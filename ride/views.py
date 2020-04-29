from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from submit.models import Rides
from django.utils import timezone
from .forms import reserveForm
from django.core.mail import send_mail
from django.conf import settings
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
         reservation.reserved = 'Reserved'
         #send email to driver
         driEmail = [reservation.driEmail]
         subject = 'Ride Offer Reserved'
         message = 'Someone accepted your ride on EDUWheels'
         email_from = settings.EMAIL_HOST_USER

         send_mail ( subject, message, email_from, driEmail )
         reservation.save()


   return HttpResponseRedirect('.')


