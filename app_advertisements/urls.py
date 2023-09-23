from django.urls import path
from .views import index, advertisement, advertisement_post, login, profile, register, top_sellers

urlpatterns = [
    path('', index, name='main_page'),
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement-post/', advertisement_post, name='advertisement_post'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('top_sellers/', top_sellers, name='top_sellers')
]