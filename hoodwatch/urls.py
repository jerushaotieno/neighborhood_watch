from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.posts_of_day,name = 'postsToday'),
]