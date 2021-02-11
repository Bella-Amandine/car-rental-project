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
    v_kind_choice = (
        ('car', 'Car'),
        ('jip', 'Jip'),
        ('truck', 'Truck'),
    )
    vehicle_kind = models.CharField(max_length= 40, choices=v_kind_choice, default='car')

    v_type_choices = (
        ('toyota', 'Toyota'),
        ('v8', 'V8'),
        ('bmw', 'BMW'),
    )
    vehicle_type = models.CharField(max_length= 40, choices=v_type_choices, default='toyota')
    number_of_passenger = models.IntegerField()

    def __str__(self):
        return self.vehicle_type

class RequestRent(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='requests')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='requests')
    comment = models.TextField()
    start_date = models.DateField("Start Date(mm/dd/yyyy)", auto_now_add=False, auto_now=False)
    return_date = models.DateField("Return Date(mm/dd/yyyy)", auto_now_add=False, auto_now=False)
    status_choice = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length= 30, choices=status_choice, default='pending')

    def __str__(self):
        return f'{self.vehicle.vehicle_type} RequestRent'
