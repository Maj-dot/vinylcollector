from django.shortcuts import render
from django.http import HttpResponse

class Vinyl:
    def __init__(self, name, artist, genre, description):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.description = description
     

vinyls = [
    Vinyl('In My Lifetime Vol.1', 'Jay-Z', 'Hip-Hop', 'One of the best albums ever!'),
    Vinyl('Experience Hendrix', 'Jimi Hendrix', 'Psychedelic Rock', 'I Love Jimi!!'),
    Vinyl('Views', 'Drake', 'Hip-Hop', 'Every Saturday Morning Type Of Vibe To Blast!!')
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def records(request):
    return render(request, 'records.html')

def vinyls(request):
    return render(request, 'vinyls/vinyls.html', {'vinyls': vinyls})