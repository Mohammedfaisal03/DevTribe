# Generated by Django 5.0.4 on 2024-07-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
