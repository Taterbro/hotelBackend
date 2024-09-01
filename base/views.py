from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import contact,Wallpaper,Room
from .serializers import contactSerializer, wallpaperSerializer


@api_view(['GET'])
def getRoutes(request):
    cont = contact.objects.all()
    serializer = contactSerializer(cont, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWallpapers(request):
    wallp = Wallpaper.objects.all()
    serializer = wallpaperSerializer(wallp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWallpaper(request, pk):
    wallp = Wallpaper.objects.get(id=pk)
    serializer = wallpaperSerializer(wallp, many=False)
    return Response(serializer.data)
# Create your views here.
