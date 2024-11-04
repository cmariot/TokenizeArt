from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    id = models.AutoField(primary_key=True, unique=True, editable=False)
    image = models.TextField(null=True, blank=True)
    usual_full_name = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


class Project(models.Model):

    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.TextField()

    def __str__(self):
        return self.name


class UserProject(models.Model):

    id = models.AutoField(primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    grade = models.IntegerField(null=True, blank=True)
    marked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.project}"
