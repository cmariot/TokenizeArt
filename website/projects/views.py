from typing import Any
from django.views.generic import TemplateView
from account.models import UserProject
from .nft import generate_nft_image
from .host import host_nft_image_on_ipfs
from .forms import NFTImageForm
from django.views.generic.edit import FormView
from openai import OpenAI
import os
import requests
from account.models import Project
import json


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

    # Define the form to ask the user for the NFT image description, it will be used to generate the NFT image
    form_class = NFTImageForm
    success_url = '/'

    # Define the template to render the form
    template_name = 'projects/templates/nft_image.html'


    def get_initial(self):
        initial = super().get_initial()
        username = self.request.user.username
        project_name = self.request.GET.get('project')
        initial['nft_prompt'] = 'Create an NFT image that represents the project completion for the 42 school project ' + project_name + ' by ' + username
        return initial


    def form_valid(self, form):

        nft_prompt = form.cleaned_data['nft_prompt']
        username = self.request.user.username
        project_name = self.request.GET.get('project')

        # Get the description of the Project from the database
        project = Project.objects.get(name=project_name)
        project_description = project.description

        print(f'{username} is creating an NFT image for the project {project_name} with the prompt: {nft_prompt}')

        ####################################
        # UNCOMMENT WHEN THE API IS WORKING
        ####################################

        client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

        system_prompt = f"Create an NFT image for the 42 project {project_name} (descritpion: {nft_prompt}) with the prompt: {nft_prompt}"

        response = client.images.generate(
            model="dall-e-3",
            prompt=system_prompt,
            size="1024x1024",
            quality="standard",
        )

        image_url = response.data[0].url
        print(f'NFT image generated: {image_url}')

        # Save the NFT image to the project folder
        image = requests.get(image_url)
        filename = f'{username}_{project_name}_nft_image.jpg'

        with open(filename, 'wb') as file:
            file.write(image.content)

        print(f'NFT image saved: {filename}')

        ####################################
        # TO REMOVE WHEN THE API IS WORKING
        ####################################

        # filename = '/home/cmariot/42/Tokenizer/website/cmariot_computorv1_nft_image.jpg'

        ####################################

        # Host the NFT image on IPFS
        import requests

        # Vos clés Pinata
        PINATA_API_KEY = os.environ.get('PINATA_API_KEY')
        PINATA_API_SECRET = os.environ.get('PINATA_API_SECRET')

        def upload_to_pinata(file_path):
            url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

            # Charger le fichier
            with open(file_path, "rb") as file:
                files = {"file": file}
                headers = {
                    "pinata_api_key": PINATA_API_KEY,
                    "pinata_secret_api_key": PINATA_API_SECRET,
                }

                # Envoyer la requête
                response = requests.post(url, files=files, headers=headers)

                if response.status_code == 200:
                    ipfs_hash = response.json()["IpfsHash"]
                    ipfs_url = f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}"
                    return ipfs_url
                else:
                    print(f"Erreur: {response.status_code}, {response.json()}")
                    return None

        ipfs_url = upload_to_pinata(filename)

        if ipfs_url:
            print(f"Image uploadée avec succès ! URL IPFS : {ipfs_url}")

            # Generate the NFT metadata
            nft_metadata = {
                'name': 'Ecole 42 Project Completion Certification',
                'description': f'This certifies that {username} has successfully completed the project {project_name}. This NFT recognizes the achievement of this project within the 42 school curriculum, reflecting {username}\'s skills and dedication.',
                'image': ipfs_url,
                'attributes': {
                    'user': username,
                    'project': project_name,
                    'description': project_description
                }
            }

            # Save the NFT metadata to the project folder
            metadata_filename = f'{username}_{project_name}_nft_metadata.json'

            with open(metadata_filename, 'w') as file:
                file.write(json.dumps(nft_metadata))

            print(f'NFT metadata saved: {metadata_filename}')

            # Save the NFT metadata on IPFS

            metadata_ipfs_url = upload_to_pinata(metadata_filename)



        else:
            print("Échec de l'upload.")


        return super().form_valid(form)


class Mint(TemplateView):

    template_name = 'projects/templates/mint.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)

        # Get the project name from the URL parameters 'project'
        project_name = self.request.GET.get('project')
        username = self.request.user.username

        # Get the user_project from the database
        user_project = UserProject.objects.filter(
            user__username=username,
            project__name=project_name
        ).first()

        if user_project:
            context['project'] = user_project
            return context

        context['message'] = 'You have not completed this project'
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if 'message' in context:
            return self.render_to_response(context)
        username = self.request.user.username
        project_name = context['project'].project.name
        project_grade = context['project'].grade
        date = context['project'].marked_at
        nft_number = 1

        # Generate the NFT image
        # Save the NFT image to the project folder
        filename = generate_nft_image(
            username, project_name, date,
            project_grade, nft_number
        )

        # Host the NFT image on IPFS
        # https://docs.pinata.cloud/api-reference/endpoint/upload-a-file
        image_url = host_nft_image_on_ipfs(filename)

        # Generate the NFT metadata
        nft_metadata = {
            'name': 'Ecole 42 Project Completion Certification',
            'description': f'This certifies that {username} has successfully completed the project {project_name} with a grade of {project_grade}. This NFT recognizes the achievement of this project within the 42 school curriculum, reflecting {username}\'s skills and dedication.',
            'image': image_url,
            'attributes': {
                'user': username,
                'project': project_name,
                'grade': project_grade
            }
        }

        # Save the NFT metadata to the project folder

        # Host the NFT metadata on IPFS

        # Mint the NFT

        return super().get(request, *args, **kwargs)
