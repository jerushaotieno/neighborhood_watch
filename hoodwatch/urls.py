from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns=[
    url('^$',views.posts_of_day,name = 'postsToday'),
]