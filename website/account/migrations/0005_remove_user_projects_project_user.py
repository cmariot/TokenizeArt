# Generated by Django 5.1.1 on 2024-11-04 14:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_projects_user_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='projects',
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
