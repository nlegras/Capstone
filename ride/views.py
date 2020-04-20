from django.shortcuts import render
from django.http import HttpResponse
from submit.models import Rides
from django.utils import timezone
# Create your views here.

def post_rides(request):
   rides = Rides.objects.all()
   return render(request, 'rides.html', {'rides': rides})

