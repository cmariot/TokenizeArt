# Generated by Django 5.1.1 on 2024-11-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_userproject_marked_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wallet',
            field=models.TextField(blank=True, null=True),
        ),
    ]
