# Generated by Django 4.1.5 on 2023-01-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_rename_titple_project_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='upadted',
            new_name='updated',
        ),
    ]
