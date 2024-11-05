from django.urls import path
from .views import Home, Mint

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('mint/', Mint.as_view(), name='mint'),
]
