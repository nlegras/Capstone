from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_rides, name='post_rides'),
    path('reserve', views.resRide, name='resRide'),
    path('<int:id>/', views.rideDetails, name='rideDetails'),
    url(r'^results/$', views.search, name='search'),
    
]