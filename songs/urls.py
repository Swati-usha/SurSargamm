from django.urls import path
from . import views

app_name = 'songs'

urlpatterns = [
     path('', views.sangeet, name='sangeet'),
     path('create/',views.createmysongs,name='createmysongs'),
]
