from django.db import models
from datetime import datetime

# Create your models here.
class FlightPassenger(models.Model):
    GENDER = [('Male', 'Male'), ('Female', 'Female')]
    full_name = models.CharField(max_length=100, null=True, blank=False)
    gender = models.CharField(max_length=50, null=True, blank=False, choices=GENDER)
    date_of_birth = models.DateField(default=datetime(), null=True, blank=False)
    nationality = models.CharField(max_length=10, null=True, blank=False)
    phone_number = models.PositiveIntegerField(default=0, null=True, blank=False)
    email_address = models.CharField(max_length=255, null=True, blank=False)
    box_number = models.CharField(max_length=100)
    emmergency_phone_number = models.PositiveIntegerField(default=0,null=True, blank=False)
    passport_number = models.PositiveIntegerField(default=0, null=True, blank=False)
    visa_documents = models.FileField(upload= '/uploads')
    departure_city = models.CharField(max_length=255, null=True, blank=False)
    destination_city = models.CharField(max_length=255, null=True, blank=False)

    def _str_(self): 
        return self.full_name