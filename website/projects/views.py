from django.views.generic import TemplateView
from account.models import UserProject
from .forms import NFTImageForm
from django.views.generic.edit import FormView
from openai import OpenAI
import os
import requests
import json
from django.shortcuts import redirect
from django.conf import settings
import subprocess


class Home(TemplateView):

    template_name = 'projects/templates/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            search = self.request.GET.get('search')
            if search:
                context['projects'] = UserProject.objects.filter(
                    user=self.request.user,
                    project__name__icontains=search
                )
            else:
                context['projects'] = UserProject.objects.filter(
                    user=self.request.user
                )
        return context


class CreateNFTImage(FormView):

    form_class = NFTImageForm
    template_name = 'projects/templates/nft_image.html'
    success_url = '/nft/view/'


    def get_initial(self):
        initial = super().get_initial()
        username = self.request.user.username
        project_name = self.request.GET.get('project')
        if not project_name or not username:
            return redirect('home')
        initial['nft_prompt'] = 'Create an NFT image that represents the project completion for the 42 school project ' + project_name
        return initial


    def form_valid(self, form):

        debug = False

        if debug:
            return super().form_valid(form)

        username = self.request.user.username
        project_name = self.request.GET.get('project')
        if not project_name or not username:
            return redirect('home')

        nft_prompt = form.cleaned_data['nft_prompt']
        system_prompt = f"{nft_prompt}. The generated image must have the number 42 in it."

        try:

            # Generate the NFT image using OpenAI's DALL-E model
            client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
            print(f'Generating NFT image with prompt: {system_prompt}')
            response = client.images.generate(
                model="dall-e-3",
                prompt=system_prompt,
                size="1024x1024",
                quality="standard",
            )
            image_url = response.data[0].url
            print(f'NFT image generated: {image_url}')
            image = requests.get(image_url)
            filename = f'{settings.STATICFILES_DIRS[0]}/nft/images/{username}_{project_name}_nft_image.jpg'
            with open(filename, 'wb') as file:
                file.write(image.content)
            print(f'NFT image saved: {filename}')

            # Upload the NFT image to IPFS
            PINATA_API_KEY = os.environ.get('PINATA_API_KEY')
            PINATA_API_SECRET = os.environ.get('PINATA_API_SECRET')

            def upload_to_pinata(file_path):
                url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
                with open(file_path, "rb") as file:
                    files = {"file": file}
                    headers = {
                        "pinata_api_key": PINATA_API_KEY,
                        "pinata_secret_api_key": PINATA_API_SECRET,
                    }
                    response = requests.post(url, files=files, headers=headers)
                    if response.status_code == 200:
                        ipfs_hash = response.json()["IpfsHash"]
                        ipfs_url = f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}"
                        return ipfs_url
                    else:
                        print(f"Erreur: {response.status_code}, {response.json()}")
                        return None

            # Upload the NFT image to IPFS
            ipfs_url = upload_to_pinata(filename)

            if ipfs_url:
                print(f"Image uploadée avec succès ! URL IPFS : {ipfs_url}")

                nft_metadata = {
                    "description": f'This NFT certifies that {username} has successfully completed the project {project_name}. This NFT recognizes the achievement of this project within the 42 school curriculum, reflecting {username}\'s skills and dedication.',
                    "external_url": "https://42.fr",
                    "image": ipfs_url,
                    "name": "Ecole 42 Project Completion Certification",
                    "attributes": {
                        'artist’s name': 'cmariot',
                        'user': username,
                        'project': project_name,

                    }
                }
                # Save the NFT metadata to the static/metadatas folder
                metadata_filename = f'{settings.STATICFILES_DIRS[0]}/nft/metadatas/{username}_{project_name}_nft_metadata.json'
                with open(metadata_filename, 'w') as file:
                    file.write(json.dumps(nft_metadata))
                print(f'NFT metadata saved: {metadata_filename}')

                # Save the NFT metadata on IPFS
                metadata_ipfs_url = upload_to_pinata(metadata_filename)

                # Save the NFT metadata to the database
                user_project = UserProject.objects.filter(
                    user__username=username,
                    project__name=project_name
                ).first()
                if user_project:
                    user_project.ipfs_metadata = metadata_ipfs_url
                    user_project.save()

                # Visualize the NFT image and metadata
                print(f'NFT metadata uploadée avec succès ! URL IPFS : {metadata_ipfs_url}')

            response = super().form_valid(form)

            # Redirect to the NFT image visualization page
            response['Location'] = f'/nft/view/?project={project_name}'

            return response

        except Exception as e:
            print(f'Error: {e}')
            return redirect('home')


    def post(self, request, *args, **kwargs):
        # If user is not authenticated, redirect to the login page
        if not self.request.user.is_authenticated:
            return redirect('login')

        # Get the project name from the URL parameters 'project'
        project_name = self.request.GET.get('project')
        username = self.request.user.username

        # Get the user_project from the database
        user_project = UserProject.objects.filter(
            user__username=username,
            project__name=project_name
        ).first()
        if not user_project:
            return redirect('home')
        super().post(request, *args, **kwargs)
        return redirect(f'/nft/view/?project={project_name}')


class ViewNFTImage(TemplateView):

    template_name = 'projects/templates/view_nft_image.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.user.username
        project_name = self.request.GET.get('project')
        if not project_name or not username:
            redirect('home')
        context['username'] = username
        context['project_name'] = project_name
        metadata_filename = f'{settings.STATICFILES_DIRS[0]}/nft/metadatas/{username}_{project_name}_nft_metadata.json'
        if not os.path.exists(metadata_filename):
            print(f'Error: NFT metadata file not found: {metadata_filename}')
            return redirect('home')
        with open(metadata_filename, 'r') as file:
            metadata = json.load(file)
            context['nft_metadata'] = metadata
        nft_image_filename = f'{settings.STATICFILES_DIRS[0]}/nft/images/{username}_{project_name}_nft_image.jpg'
        if not os.path.exists(nft_image_filename):
            return redirect('home')
        context['nft_image_url'] = nft_image_filename
        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class Mint(TemplateView):

    template_name = 'projects/templates/mint.html'

    def get(self, request, *args, **kwargs):

        # If user is not authenticated, redirect to the login page
        if not self.request.user.is_authenticated:
            return redirect('login')
        user = self.request.user

        # Get the project name from the URL parameters 'project'
        project_name = self.request.GET.get('project')
        if not project_name:
            return redirect('home')

        # Get the user_project from the database
        user_project = UserProject.objects.filter(
            user=user,
            project__name=project_name
        ).first()

        if not user_project:
            return redirect('home')

        nft_metadatas = f'{settings.STATICFILES_DIRS[0]}/nft/metadatas/{user.username}_{project_name}_nft_metadata.json'

        if not os.path.exists(nft_metadatas):
            return redirect('home')

        with open(nft_metadatas, 'r') as file:
            nft_metadatas = json.load(file)

        context = {
            'username': user.username,
            'wallet': user.wallet,
            'project_name': project_name,
            'nft_metadatas': nft_metadatas,
        }

        # Call the mint script to mint the NFT
        mint_script = f'{settings.BASE_DIR}/../code/'

        if os.path.exists(mint_script):

            metadata_url = user_project.ipfs_metadata
            if not metadata_url:
                return redirect('home')

            command = ['yarn', 'hardhat', 'mint', '--to', f'{user.wallet}', '--uri', f'{metadata_url}']

            try:
                saved_path = os.getcwd()
                os.chdir(mint_script)
                result = subprocess.run(command, text=True, capture_output=True, check=True)
                output = result.stdout
                # print("Output de la commande :", output)
                output = output.split("\n")
                hash = ""
                for line in output:
                    if "hash:" in line:
                        hash = line.split(": ")[-1]
                        break
                hash = hash.replace("'", "")
                hash = hash.replace(",", "")
                hash = "https://sepolia.etherscan.io/tx/" + hash
                context['hash'] = hash
                os.chdir(saved_path)
            except subprocess.CalledProcessError as e:
                print("Erreur lors de l'exécution de la commande :", e.stderr)
                os.chdir(saved_path)

        return self.render_to_response(context)
