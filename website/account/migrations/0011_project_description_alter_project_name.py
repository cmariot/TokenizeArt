# Generated by Django 5.1.1 on 2024-11-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_user_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
