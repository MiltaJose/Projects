# Generated by Django 4.2.9 on 2024-03-04 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='desc',
            new_name='team_desc',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='img',
            new_name='team_img',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='team_name',
        ),
    ]