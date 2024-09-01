from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('wallp/', views.getWallpapers, name='wallps'),
    path('wallp/<str:pk>/', views.getWallpaper, name='wallp')
]