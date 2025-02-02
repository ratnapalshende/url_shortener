from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shorten/', views.shorten_url, name='shorten'),
    path('<str:short_code>/', views.redirect_url, name='redirect'),
    path('delete/<str:short_code>/', views.delete_url, name='delete'),
]

