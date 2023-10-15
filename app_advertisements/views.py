from django.shortcuts import render, redirect
from .models import Advertisement
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AdvertisementForm
from django.urls import reverse

def index(request):
    title = request.GET.get('query')
    if title:
        advs = Advertisement.objects.filter(title__contains=title)
    else:
        advs = Advertisement.objects.all()
    context = {'advertisements': advs}
    return render(request, 'app_advertisements/index.html', context)

def advertisement(request):
    return render(request, 'app_advertisements/advertisement.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        form.fields['image'].initial = '/static/img/pict.png'
        if form.is_valid():
            # advertisement = Advertisement(**form.cleaned_data)
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

def game(request):
    return render(request, 'game.html')

