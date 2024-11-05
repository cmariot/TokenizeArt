from django.urls import path
from .views import Login, Logout, UpdateWallet

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('wallet/<pk>', UpdateWallet.as_view(), name='wallet'),
]
