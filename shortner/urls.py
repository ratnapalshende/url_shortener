from django.urls import path
from .views import ShortenURLView, ShortURLStatsView, create_short_url, redirect_url

urlpatterns = [
    path('shorten/', create_short_url, name='create_short_url'),
    path('shorten/<str:short_code>/', ShortenURLView.as_view(), name='retrieve'),
    path('shorten/<str:short_code>/stats/', ShortURLStatsView.as_view(), name='stats'),
    path('<str:short_code>/', redirect_url, name='redirect_url'),
]
