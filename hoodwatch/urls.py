from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

    # url(r'^hoods/', views.hoods, name = 'hoods'),
    # url('^$',views.posts_of_day,name = 'postsToday'),



urlpatterns=[
    url('^$',views.hoods, name = 'hoods'),
    url(r'^posts/', views.posts_of_day, name = 'postsToday'),
    url(r'^business/', views.business, name = 'business'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)