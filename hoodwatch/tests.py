from django.test import TestCase

from hoodwatch.views import posts_of_day
from . models import Neighborhood, Profile, Business, Post
from django.contrib.auth.models import User
import datetime as dt


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


# Post Class Tests

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Profile(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_profile()

        # Creating a new post and saving it

        self.new_post= Post(title = 'Test Post',post = 'This is a random test Post',editor = self.james)
        self.new_post.save()

    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()

    # Getting today's posts 
    def test_get_posts_of_day(self):
        posts_of_day = Post.posts_of_day()
        self.assertTrue(len(posts_of_day)>0)


    def test_get_posts_by_date(self):
        test_date = '2022-04-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        posts_by_date = Post.days_posts(date)
        self.assertTrue(len(posts_by_date) == 0)