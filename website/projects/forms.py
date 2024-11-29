from django import forms


class NFTImageForm(forms.Form):
    nft_prompt = forms.CharField(
        label='Dall-E 3 Prompt to generate your NFT image'
    )
