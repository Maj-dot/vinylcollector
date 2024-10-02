from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vinyl
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
        
            