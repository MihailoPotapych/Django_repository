from django.urls import path
from .views import index, advertisement, advertisement_post, top_sellers, game

urlpatterns = [
    path('', index, name='main_page'),
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement-post/', advertisement_post, name='advertisement_post'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('game/', game, name='game')
]