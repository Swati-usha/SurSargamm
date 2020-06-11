from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
   Title = models.CharField(max_length=100)
   description =models.CharField(max_length=250)
   image = models.ImageField()
   url = models.URLField()


   def __str__(self):
         return self.Title



class MySongs(models.Model):
    PlaylistName = models.CharField(max_length = 100)
    Link = models.URLField()
    created = models.DateTimeField(auto_now_add = True)
    DateCompleted = models.DateTimeField(null = True, blank= True)
    Favourite = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.PlaylistName 
