from django.shortcuts import render
from .models import Advertisement
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    advs = Advertisement.objects.all()
    context = {'advertisements': advs}
    return render(request, 'index.html', context)

def advertisement(request):
    return render(request, 'advertisement.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')
