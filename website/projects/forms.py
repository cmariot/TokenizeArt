from django import forms


class NFTImageForm(forms.Form):
    nft_prompt = forms.CharField(
        label='NFT Prompt',
    )
