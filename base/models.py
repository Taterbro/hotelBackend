from django.db import models


class Wallpaper(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='img', default='placeholder')
    isActive = models.BooleanField(default=False)

class Room(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='img', default='placeholder')
    isActive = models.BooleanField(default=False)
    roomName = models.CharField(max_length=25, null=True)
    description = models.TextField(blank=True, null= False)

class contact(models.Model):
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    mapsLink = models.URLField()

    


# Create your models here.
