from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome To My Vinyl Shop</h1>')

def records(request):
    return HttpResponse('<h1>My Records</h1>')