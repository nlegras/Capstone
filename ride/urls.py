from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_rides, name='post_rides'),
]