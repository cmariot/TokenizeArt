from typing import Any
from django.views.generic import TemplateView
from account.models import UserProject


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

        # Generate the NFT image

        # Save the NFT image to the project folder

        # Host the NFT image on IPFS
        # https://docs.pinata.cloud/api-reference/endpoint/upload-a-file
        image_url = ''

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
