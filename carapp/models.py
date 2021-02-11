from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profile')
    profile_picture = models.ImageField(upload_to = 'profiles/', blank= True)
    full_name = models.CharField(max_length= 100, blank= True)
    contact = models.CharField(max_length= 255)

    def __str__(self):
        return f'{self.user.username} profile'

    def create_profile(self):
        self.save()

    @classmethod
    def updateProfile(cls, id, new_profile):
        cls.objects.filter(id = id).update(profile_picture = new_profile.profile_picture,
                                           full_name = new_profile.full_name,
                                           contact = new_profile.contact)

    @classmethod
    def get_profile_by_id(cls, id):
        return cls.objects.get(pk = id)

class Vehicle(models.Model):
    v_kind_choice = (
        ('car', 'Car'),
        ('jip', 'Jip'),
        ('truck', 'Truck'),
    )

    v_type_choices = (
        ('toyota', 'Toyota'),
        ('v8', 'V8'),
        ('bmw', 'BMW'),
    )

    status_choice = (
        ('available', 'Available'),
        ('busy', 'Busy'),
    )

    owner = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='vehicles')
    vehicle_picture = models.ImageField(upload_to= 'vehicles/')
    vehicle_color = models.CharField(max_length=100)
    vehicle_kind = models.CharField(max_length= 40, choices=v_kind_choice, default='car')
    vehicle_type = models.CharField(max_length= 40, choices=v_type_choices, default='toyota')
    number_of_passenger = models.IntegerField()
    status_of_vehicle = models.CharField(max_length= 40, choices= status_choice, default='available')

    def __str__(self):
        return self.vehicle_type

    def save_vehicle(self):
        self.save()

    @classmethod
    def get_all_available_vehicles(cls):
        return cls.objects.filter(status_of_vehicle = 'available')

    def set_vehicle_available(self):
        Vehicle.objects.filter(id = self.id).update(status_of_vehicle = 'available')

    def set_vehicle_busy(self):
        Vehicle.objects.filter(id = self.id).update(status_of_vehicle = 'busy')


class RequestRent(models.Model):
    status_choice = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='requests')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='requests')
    comment = models.TextField()
    start_date = models.DateField("Start Date(mm/dd/yyyy)", auto_now_add=False, auto_now=False)
    return_date = models.DateField("Return Date(mm/dd/yyyy)", auto_now_add=False, auto_now=False)
    status = models.CharField(max_length= 30, choices=status_choice, default='pending')

    def __str__(self):
        return f'{self.vehicle.vehicle_type} RequestRent'

    def create_request(self):
        self.save()

    @classmethod
    def get_all_requests_by_vehicle_owner(cls, username):
        return cls.objects.filter(vehicle__owner__user__username = username)

    @classmethod
    def approve_request(cls, id):
        cls.objects.filter(id = id).update(status = 'approved')

    @classmethod
    def reject_request(cls, id):
        cls.objects.filter(id=id).update(status='rejected')

