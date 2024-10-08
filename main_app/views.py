from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Vinyl, Playlist, Song
from .forms import SongForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyls(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/vinyls.html', {'vinyls': vinyls})

def vinyl_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    song_form = SongForm()
    return render(request, 'vinyls/detail.html', {
        'vinyl': vinyl, 'song_form': song_form
    })

class VinylCreate(CreateView):
    model = Vinyl
    fields = '__all__'
    success_url = '/vinyls/'
    
class VinylUpdate(UpdateView):
    model = Vinyl
    fields = ['genre', 'description']
    
class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls/'        

def add_song(request, vinyl_id):
    form = SongForm(request.POST)
    if form.is_valid():
        new_song = form.save(commit=False)
        new_song.vinyl_id = vinyl_id    
        new_song.save()
    return redirect('vinyl-detail', vinyl_id=vinyl_id)    
        
class PlaylistCreate(CreateView):
    model = Playlist
    fields = ['name', 'description']
    
class PlaylistList(ListView):
    model = Playlist
    
class PlaylistDetail(DetailView):
    model = Playlist
    # commented out below, detail page now works, but song form giving errors.
    template_name = 'main_app/playlist_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = Song.objects.all()
        return context 

def add_playlist_song(request, playlist_id, song_id):
    Playlist.objects.get(id=playlist_id).songs.add(song_id)
    return redirect('playlist-detail', pk=playlist_id)

def remove_playlist_song(request, playlist_id, song_id):
    playlist = Playlist.objects.get(id=playlist_id)
    song = Song.objects.get(id=song_id)
    playlist.songs.remove(song)
    return redirect('playlist-detail', pk=playlist_id)  
      
class PlaylistUpdate(UpdateView):
    model = Playlist
    fields = '__all__'
    
class PlaylistDelete(DeleteView):
    model = Playlist
    success_url = '/playlist/'
    
  