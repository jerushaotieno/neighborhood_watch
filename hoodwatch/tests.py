from django.test import TestCase
from . models import Neighborhood, Profile, Business, Post
from django.contrib.auth.models import User


# Create your tests here.

# Neighborhood Class Tests

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.new_neighborhood=Neighborhood(name='Madaraka')

    def tearDown(self):
        Neighborhood.objects.all().delete()

    # test for instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood, Neighborhood))

    # test for save method
    def test_save_neighborhood(self):
        self.new_neighborhood.create_neigborhood()
        neighborhood=Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)>0)

    def test_delete_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        self.new_neighborhood.delete_neighborhood()
        neighborhood=Neighborhood.objects.all()
        self.assertEqual(len(neighborhood),0)


# Profile Class Tests

class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User(name="James", email="jamesjoe@gmail.com", password="12345")
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user,image="image.jpeg",bio="sample testing")

    # test for instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    # test save method
    def test_save_profile(self):
        self.new_profile.create_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>0)