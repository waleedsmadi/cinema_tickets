from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    date = models.DateField()


class Guest(models.Model):
    name = models.CharField(max_length=30)
    mobile = PhoneNumberField(null=False, blank=False, unique=True)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservation')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reservation')
