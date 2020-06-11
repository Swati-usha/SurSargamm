from django.db import models

class Poetry(models.Model):
    Title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length = 100)

    def __str__(self):
        return self.Title
