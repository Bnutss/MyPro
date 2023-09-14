from django.urls import path
from .views import *

app_name = 'warcraft'
urlpatterns = [
    path('', StartView.as_view(), name='start_pages'),
    path('about/', AboutView.as_view(), name='about_pages'),
    path('gallery/', GalleryView.as_view(), name='gallery_pages'),
    path('video/', VideoView.as_view(), name='video_pages'),
]
