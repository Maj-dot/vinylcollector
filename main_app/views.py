from django.shortcuts import render
from .models import Vinyl


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
    return render(request, 'vinyls/detail.html', {'vinyl': vinyl})