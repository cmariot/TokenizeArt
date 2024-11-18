from django.urls import path
from .views import Home, Mint, CreateNFTImage, ViewNFTImage

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('nft/create/', CreateNFTImage.as_view(), name='create_nft_image'),
    path('nft/view/', ViewNFTImage.as_view(), name='view_nft_image'),
    path('nft/mint/', Mint.as_view(), name='mint'),
]
