# Generated by Django 5.0.1 on 2024-08-23 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='isFeatured',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='wallpaper',
            old_name='isFeatured',
            new_name='isActive',
        ),
    ]
