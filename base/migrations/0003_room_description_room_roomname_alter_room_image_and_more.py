# Generated by Django 5.0.1 on 2024-08-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_isfeatured_room_isactive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='roomName',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, default='placeholder', null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='image',
            field=models.ImageField(blank=True, default='placeholder', null=True, upload_to='img'),
        ),
    ]
