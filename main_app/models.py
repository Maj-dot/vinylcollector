from django.db import models
from django.urls import reverse

MOOD_CHOICES = (
    ('T', 'Turn Up'),
    ('C', 'Calm Vibes'),
    ('R', 'Romantic Vibes'),
    ('P', 'Productive Tunes'),
    ('S', 'Sad Vibes')
)

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
    
    
class Song(models.Model):
    date = models.DateField('Latest Listening date')
    title = models.CharField(max_length=100)
    duration = models.TimeField('Song Duration', max_length=10)
    mood = models.CharField(
        max_length=20, 
        choices=MOOD_CHOICES,
        default=MOOD_CHOICES[1][1]
    )
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_mood_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
        
        
class Playlist(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('playlist-detail', kwargs={"pk": self.id})
    
          
        
        