from django.shortcuts import render, redirect
from django.http  import Http404, HttpResponse
import datetime as dt
from .models import Post


# Create your views here.
def welcome(request):
    return render(request, 'index.html')


# View Function to present posts from past days
def posts_of_day(request):
    date = dt.date.today()
    hoodwatch = Post.objects.all()
    return render(request, 'all-posts/today-posts.html', {"date": date, "hoodwatch":hoodwatch})


# View Function to present posts from past days
def past_days_posts(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(posts_of_day)

    hoodwatch = Post.days_posts(date)
    return render(request, 'all-posts/past-posts.html', {"date": date, "hoodwatch":hoodwatch})
