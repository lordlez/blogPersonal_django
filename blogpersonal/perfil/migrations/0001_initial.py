# Generated by Django 4.1.5 on 2023-01-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titple', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
    ]
