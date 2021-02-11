from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  .models import Profile, Vehicle, RequestRent

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['owner', 'status_of_vehicle']

class RequestRentForm(forms.ModelForm):
    class Meta:
        model = RequestRent
        exclude = ['user', 'vehicle', 'status']