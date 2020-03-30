from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    
    TURF_USER = 'TU'
    TURF_OWNER = 'TO'
    ROLE_TYPE_CHOICES = [
        (TURF_USER, 'TURF USER'),
        (TURF_OWNER, 'TURF OWNER'),
    ]
    role_type = models.CharField(max_length= 2, choices=ROLE_TYPE_CHOICES, default=TURF_USER)
    
class Turf(models.Model):
    turf_name = models.CharField(max_length=25)
    turf_location = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=2, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   

class Booking(models.Model):
    players = models.IntegerField()
    time_booked = models.DateTimeField()
    status = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    
class Schedule(models.Model):
    DAYS = (
        ('MON', 'MONDAY'),
        ('TUE', 'TUESDAY'),
        ('WED', 'WEDNESDAY'),
        ('THUR', 'THURSDAY'),
        ('FRI', 'FRIDAY')
    )
    time_slot_one = models.TimeField()
    time_slot_two = models.TimeField()
    time_slot_three = models.TimeField()
    day = models.CharField(max_length=4, choices=DAYS)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)

class Tournament(models.Model):
    tournament_name = models.CharField(max_length=30)
    tournament_prize = models.IntegerField()
    tournament_poster = CloudinaryField('tournament_poster')
    tournament_date = models.DateField()
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

       
