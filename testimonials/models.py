from django.db import models

class Testimonials(models.Model):
    Name  = models.CharField(max_length = 20)
    Message = models.CharField(max_length = 200)
