from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    TURF_USER = 'TU'
    TURF_OWNER = 'TO'
    ROLE_TYPE_CHOICES = [
        (TURF_USER, 'TURF USER'),
        (TURF_OWNER, 'TURF OWNER'),
    ]
    role_type = models.CharField(max_length= 2, choices=ROLE_TYPE_CHOICES, default=TURF_USER)
    
