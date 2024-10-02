from django.db import models
from django.urls import reverse

# Create your models here.
class Vinyl(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse("vinyl-detail", kwargs={"vinyl_id": self.id})
    