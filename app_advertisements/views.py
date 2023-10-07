from django.shortcuts import render, redirect
from .models import Advertisement
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AdvertisementForms
from django.urls import reverse

def index(request):
    advs = Advertisement.objects.all()
    context = {'advertisements': advs}
    return render(request, 'app_advertisements/index.html', context)

def advertisement(request):
    return render(request, 'app_advertisements/advertisement.html')

def advertisement_post(request):
    if request.method == 'POST':
        print('post-request')
        form = AdvertisementForms(request.POST, request.FILES)
        form.fields['image'].initial = '/static/img/pict.png'
        if form.is_valid():
            print('valid')
            # advertisement = Advertisement(**form.cleaned_data)
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        print('unvalid')
        form = AdvertisementForms()
    form = AdvertisementForms()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

def game(request):
    return render(request, 'game.html')

