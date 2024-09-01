from rest_framework.serializers import ModelSerializer
from .models import Wallpaper, contact, Room

class contactSerializer(ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'

class wallpaperSerializer(ModelSerializer):
    class Meta:
        model = Wallpaper
        fields = '__all__'

class roomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'