from django.test import TestCase
from django.test import TransactionTestCase
from .models import Profile, Vehicle, RequestRent
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.new_user = User(username = 'amandine')
        self.new_user.save()

        self.new_profile = Profile(user = self.new_user,
                                   profile_picture = 'default.jpg',
                                   full_name = 'Amandine', contact = '0789479347')
    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_create_profile_method(self):
        self.new_profile.create_profile()
        profiles = Profile.objects.all()
        self.assertTrue((len(profiles) > 0))

    def test_update_profile(self):
        self.new_profile.create_profile()
        self.updated_profile = Profile.get_profile_by_id(self.new_profile.id)
        self.updated_profile.full_name = 'Bella'

        Profile.updateProfile(self.new_profile.id, self.updated_profile)
        prof = Profile.get_profile_by_id(self.new_profile.id)

        self.assertEqual(prof.full_name, 'Bella')

class VehicleTestCase(TestCase):
    def setUp(self):
        self.new_user = User(username = 'amandine')
        self.new_user.save()

        self.new_profile = Profile(user = self.new_user,
                                   profile_picture = 'default.jpg',
                                   full_name = 'Amandine', contact = '0789479347')
        self.new_profile.create_profile()

        self.new_vehicle = Vehicle(owner = self.new_profile, vehicle_picture = 'default.jpg',
                                   vehicle_color = 'black', number_of_passenger = 5)

    def tearDown(self):
        Profile.objects.all().delete()
        Vehicle.objects.all().delete()

    def test_save_vehicle(self):
        self.new_vehicle.save_vehicle()
        vehicles = Vehicle.objects.all()
        self.assertTrue(len(vehicles) > 0)

    def test_get_all_available_vehicles(self):
        self.new_vehicle.save_vehicle()

        self.new_vehicle2 = Vehicle(owner=self.new_profile, vehicle_picture='default.jpg',
                                    vehicle_color='black', number_of_passenger=5,
                                    status_of_vehicle='busy')
        self.new_vehicle2.save_vehicle()

        vehicles = Vehicle.get_all_available_vehicles()
        self.assertTrue(len(vehicles) == 1)

    def test_set_vehicle_available(self):
        self.new_vehicle.save_vehicle()

        self.new_vehicle2 = Vehicle(owner=self.new_profile, vehicle_picture='default.jpg',
                                    vehicle_color='black', number_of_passenger=5,
                                    status_of_vehicle='busy')
        self.new_vehicle2.save_vehicle()

        self.new_vehicle2.set_vehicle_available()

        vehicles = Vehicle.get_all_available_vehicles()
        self.assertTrue(len(vehicles) == 2)

    def test_set_vehicle_busy(self):
        self.new_vehicle.save_vehicle()
        self.new_vehicle.set_vehicle_busy()
        vehicles = Vehicle.get_all_available_vehicles()
        self.assertTrue(len(vehicles) == 0)

class RequestRentTestCase(TransactionTestCase):
    def setUp(self):
        self.new_user = User(username = 'amandine')
        self.new_user.save()

        self.new_profile = Profile(user = self.new_user,
                                   profile_picture = 'default.jpg',
                                   full_name = 'Amandine', contact = '0789479347')
        self.new_profile.create_profile()

        self.new_vehicle = Vehicle(owner = self.new_profile, vehicle_picture = 'default.jpg',
                                   vehicle_color = 'black', number_of_passenger = 5)
        self.new_vehicle.save_vehicle()

        self.new_req = RequestRent(user = self.new_profile, vehicle = self.new_vehicle,
                                   comment = 'voyage', start_date = '2000-12-12',
                                   return_date = '2000-12-24')

    def tearDown(self):
        Profile.objects.all().delete()
        Vehicle.objects.all().delete()
        RequestRent.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_req, RequestRent))

    def test_create_req(self):
        self.new_req.create_request()
        all_requests = RequestRent.objects.all()
        self.assertTrue(len(all_requests) > 0)

    def test_get_all_request_by_vehicle_owner(self):
        self.new_req.create_request()

        self.new_user2 = User(username='alie')
        self.new_user2.save()

        self.new_profile2 = Profile(user=self.new_user2,
                                   profile_picture='default.jpg',
                                   full_name='Eliane', contact='0789479347')
        self.new_profile2.create_profile()

        self.new_vehicle2 = Vehicle(owner=self.new_profile2, vehicle_picture='default.jpg',
                                   vehicle_color='black', number_of_passenger=5)
        self.new_vehicle2.save_vehicle()

        all_requests = RequestRent.get_all_requests_by_vehicle_owner(self.new_profile2.user.username)
        self.assertTrue(len(all_requests) == 0)

    def test_approve_request(self):
        self.new_req.create_request()
        RequestRent.approve_request(self.new_req.id)
        req = RequestRent.objects.get(pk = self.new_req.id)
        self.assertEqual(req.status, 'approved')

    def test_reject_request(self):
        self.new_req.create_request()
        RequestRent.reject_request(self.new_req.id)
        req = RequestRent.objects.get(pk = self.new_req.id)
        self.assertEqual(req.status, 'rejected')


