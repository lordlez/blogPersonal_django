# Generated by Django 4.1.5 on 2023-01-12 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_project_created_project_upadted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='titple',
            new_name='title',
        ),
    ]
