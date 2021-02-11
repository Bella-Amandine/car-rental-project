from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profile')
    profile_picture = models.ImageField(upload_to = 'profiles/', blank= True)
    full_name = models.CharField(max_length= 100, blank= True)
    contact = models.CharField(max_length= 255)

    def __str__(self):
        return f'{self.user.username} profile'
class Vehicle(models.Model):
    owner = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='vehicles')
    vehicle_picture = models.ImageField(upload_to= 'vehicles/')
    vehicle_color = models.CharField(max_length=100)
    vehicle_kind = models.CharField(max_length= 100)
    vehicle_type = models.CharField(max_length= 100)
    number_of_passenger = models.IntegerField()

    def __str__(self):
        return self.vehicle_type

