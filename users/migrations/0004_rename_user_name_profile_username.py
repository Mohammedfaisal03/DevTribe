# Generated by Django 5.0.4 on 2024-07-20 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_name',
            new_name='username',
        ),
    ]
