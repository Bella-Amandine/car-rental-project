from django.shortcuts import render, redirect
from .forms import SignupForm, PostVehicleForm, RequestRentForm
from .models import Profile, Vehicle, RequestRent

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            new_user = form.save()

            new_profile = Profile(user = new_user)
            new_profile.create_profile()

            return redirect('login')
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})

def index(request):
    available_vehicles = Vehicle.get_all_available_vehicles()

    return render(request, 'car/index.html', {'vehicles': available_vehicles})

def post_vehicle(request):
    if request.method == 'POST':
        form = PostVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            new_vehicle = form.save(commit=False)
            new_vehicle.owner = request.user.profile
            new_vehicle.save()

            return redirect('index')
    else:
        form = PostVehicleForm()
        return render(request, 'car/new-vehicle.html', {'form': form})

def single_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk = vehicle_id)
    #Check if not found and redirect to 404 page
    if request.method == 'POST':
        pass
    else:
        form = RequestRentForm()
        return render(request, 'car/vehicle-page.html', {'vehicle' : vehicle, 'form': form})