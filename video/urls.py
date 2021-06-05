from django.urls import path
from video import views

app_name = 'video'

urlpatterns = [
    path('videolist/<int:user_id>/', views.videolist, name='videolist'),
    path('course_videolist/<int:course_id>/', views.course_videolist, name='course_videolist'),
    path('video_delete/<int:x_id>/', views.video_delete, name='video_delete'),
]
