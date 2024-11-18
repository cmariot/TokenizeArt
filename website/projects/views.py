from django.views.generic import TemplateView
from account.models import UserProject
from .forms import NFTImageForm
from django.views.generic.edit import FormView
from openai import OpenAI
import os
import requests
from account.models import Project
import json
from django.shortcuts import redirect

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
    success_url = '/nft/view/'

    # Define the template to render the form
    template_name = 'projects/templates/nft_image.html'


    def get_initial(self):
        initial = super().get_initial()
        username = self.request.user.username
        project_name = self.request.GET.get('project')
        if not project_name or not username:
            # Redirect to the home page if no project is specified or the user is not authenticated
            return redirect('home')

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

        # ####################################

        # # Host the NFT image on IPFS

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

            # Visualize the NFT image and metadata
            print(f'NFT metadata uploadée avec succès ! URL IPFS : {metadata_ipfs_url}')

        response = super().form_valid(form)

        # Redirect to the NFT image visualization page
        response['Location'] = f'/nft/view/?project={project_name}'

        return response

        # else:
            # print("Échec de l'upload.")

        return super().form_valid(form)

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

        print(f'Creating NFT image for {username} on project {project_name}')

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
            # Ask the user to specify a file to view
            redirect('error')


        context['username'] = username
        context['project_name'] = project_name

        # Get the user_project metadata from the file
        metadata_filename = f'{username}_{project_name}_nft_metadata.json'

        if os.path.exists(metadata_filename):
            with open(metadata_filename, 'r') as file:
                metadata = json.load(file)
                context['nft_metadata'] = metadata

        return context

    def get(self, request, *args, **kwargs):

        # If user is not authenticated, redirect to the login page
        if not self.request.user.is_authenticated:
            return redirect('login')

        print(f'Viewing NFT image for {self.request.user.username}')

        # If no nft image has been created, redirect to the nft list page
        if not os.path.exists(f'{self.request.user.username}_{self.request.GET.get("project")}_nft_image.jpg'):
            return redirect('home')

        context = self.get_context_data(**kwargs)

        context['nft_image_url'] = f'/static/{self.request.user.username}_{self.request.GET.get("project")}_nft_image.jpg'

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

        # Get the NFT metadata from the file
        metadata_filename = f'{user.username}_{project_name}_nft_metadata.json'

        if not os.path.exists(metadata_filename):
            return redirect('home')

        with open(metadata_filename, 'r') as file:
            metadata = json.load(file)

        context = {
            'username': user.username,
            'wallet': user.wallet,
            'project_name': project_name,
            'nft_metadata': metadata
        }

        return self.render_to_response(context)
