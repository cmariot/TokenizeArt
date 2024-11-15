from typing import Any
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest, JsonResponse
import requests
import os
from .models import User, Project, UserProject


class Login(RedirectView):

    url = '/'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any):

        # Get the UID_42 and SECRET_42 from the environment
        UID_42 = os.environ.get('UID_42')
        SECRET_42 = os.environ.get('SECRET_42')

        # Get the code from the request object
        code = request.GET.get('code')

        # Get the access token from the 42 API
        req = requests.post(
            "https://api.intra.42.fr/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": UID_42,
                "client_secret": SECRET_42,
                "code": code,
                "redirect_uri": "http://localhost:8000/account/login"
            }
        )
        if req.status_code != 200:
            return super().get(request, *args, **kwargs)
        access_token = "Bearer " + req.json()['access_token']

        # Get the user information from the 42 API
        req = requests.get(
            "https://api.intra.42.fr/v2/me",
            headers={
                "Authorization": access_token
            }
        )
        if req.status_code != 200:
            return super().get(request, *args, **kwargs)

        json = req.json()
        # print(json)

        username = json['login']

        user = User.objects.filter(username=username).first()
        if not user:
            user = User.objects.create_user(
                username=username,
                password="",
                email=json['email'],
                usual_full_name=json['usual_full_name'],
                image=json['image']['link'],
            )
            user.save()

        user = authenticate(username=username, password="")
        login(request, user)

        projects_users = json['projects_users']
        for project in projects_users:

            project_id = project['project']['id']
            project_name = project['project']['name']
            project_grade = project['final_mark']
            project_status = project['status']
            project_marked_at = project['marked_at']

            if project_status != 'finished':
                continue

            # # GET /v2/projects/{id}
            # # /v2/projects/:project_id/projects
            # req = requests.get(
            #     f"https://api.intra.42.fr/v2/cursus/1/projects",
            #     headers={
            #         "Authorization": access_token
            #     }
            # )

            # if req.status_code != 200:
            #     continue

            # print(req.json())
            # return

            #     try:
            #         project_description = project_infos['description']
            #     except KeyError:
            #         project_infos = "No description"
            # else:
            #     project_description = "No description"

            # print(f"{project_name} - {project_description}")

            # Check if the project exists in the database
            filtered_project = Project.objects.filter(name=project_name)
            if not filtered_project:
                _project = Project.objects.create(
                    name=project_name,
                    description="No description",
                )
                _project.save()


            _project = Project.objects.filter(name=project_name).first()
            user_project = UserProject.objects.filter(
                user=user,
                project=_project
            ).first()

            if not user_project:
                user_project = UserProject.objects.create(
                    user=user,
                    project=_project,
                    grade=project_grade,
                    marked_at=project_marked_at
                )
                user_project.save()
            else:
                user_project.grade = project_grade
                user_project.marked_at = project_marked_at
                user_project.save()

        return super().get(request, *args, **kwargs)


class Logout(LogoutView):

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        logout(request)
        return JsonResponse({
            'message': 'You have been logged out'
        })


class UpdateWallet(UpdateView):

    model = User
    fields = ['wallet']
    template_name = 'account/templates/update_wallet.html'
    success_url = '/'

    def form_valid(self, form):
        # Check if the user is authenticated and if the user is the same
        if (
            not self.request.user.is_authenticated or
            self.request.user != form.instance
        ):
            return super().form_invalid(form)
        self.object = form.save(commit=False)
        self.object.wallet = self.object.wallet
        self.object.save()
        return super().form_valid(form)
