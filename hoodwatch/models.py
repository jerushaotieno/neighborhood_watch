import profile
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt

# Create your models here.

# Model for Neighborhood Class

class Neighborhood(models.Model):
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    local_hospital = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)


# Model for Profile Class

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


# Model for Business Class

class Business(models.Model):
    title = models.CharField(max_length=150)
    email = models.EmailField(max_length=280)
    description = models.TextField(blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    image = models.ImageField(upload_to='images/', default='default.png')

    def __str__(self):
        return f'{self.name}'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(title__icontains=search_term)
        return business

        

# Model for Post Class

class Post(models.Model):
    title = models.CharField(max_length=150, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighborhood_post')
    posted_on = models.DateTimeField(auto_now_add=True)


# Class Method to Get the Day's Posts

    @classmethod
    def posts_of_day(cls):
        today = dt.date.today()
        posts = cls.objects.filter(posted_on__date = today)
        return posts


# Class Method to Get Any Day's Posts

    @classmethod
    def days_posts(cls,date):
        posts = cls.objects.filter(posted_on__date = date)
        return posts