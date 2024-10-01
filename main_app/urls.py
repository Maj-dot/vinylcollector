from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls, name='vinyls'),
    path('vinyls/<int:vinyl_id>/', views.vinyl_detail, name='vinyl-detail'),
]