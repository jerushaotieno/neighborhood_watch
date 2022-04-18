from django.shortcuts import render, redirect
from django.http  import Http404, HttpResponse
import datetime as dt
from .models import Neighborhood, Profile, Business, Post
from .forms import NeighborhoodForm, BusinessForm

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


# View Function to present all neighborhoods

def hoods(request):

    hoodwatch = Neighborhood.objects.all()
    # print(all_hoods)
    # all_hoods = all_hoods[::-1]
    params = {
        'hoodwatch': hoodwatch,
    }
    return render(request, 'index.html', params)

    # all_hoods = Neighborhood.objects.all()
    # return render(request, 'all_hoods/today-posts.html', {"hoodwatch":all_hoods})


def create_hood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighborhoodForm()
    return render(request, 'newhood.html', {'form': form})


def single_hood(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-hood', hood.id)
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'single_hood.html', params)


def business(request):
    hoodwatch = Business.objects.all()
    params = {
        'hoodwatch': hoodwatch,
    }
    return render(request, 'business.html', params)


def create_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.admin = request.user.profile
            business.save()
            return redirect('hood')
    else:
        form = BusinessForm()
    return render(request, 'newbusiness.html', {'form': form})


