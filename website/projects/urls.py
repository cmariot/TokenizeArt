from django.urls import path
from .views import Home, Mint, CreateNFTImage

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('nft/create/', CreateNFTImage.as_view(), name='create_nft_image'),
    path('nft/view/', CreateNFTImage.as_view(), name='view_nft_image'),
    # path('nft/what/', WhatNFTImage.as_view(), name='what_nft_image'),
    path('mint/', Mint.as_view(), name='mint'),
]
