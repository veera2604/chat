from django.urls import path
from .views import video_detail

urlpatterns = [
    path('video/<int:video_id>/', video_detail, name='video_detail'),
    
]