from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls, name='vinyls'),
    path('vinyls/<int:vinyl_id>/', views.vinyl_detail, name='vinyl-detail'),
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyl-create'),
    path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyl-update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyl-delete'),
    path('vinyls/<int:vinyl_id>/add-song/', views.add_song, name='add-song'),
    path('playlist/', views.PlaylistList.as_view(), name='playlist-index'),
    path('playlist/create/', views.PlaylistCreate.as_view(), name='playlist-create'),
    path('playlist/<int:pk>/', views.PlaylistDetail.as_view(), name='playlist-detail'),
    path('playlist/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlist-update'),
    path('playlist/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlist-delete'),
    path('playlist/<int:playlist_id>/add-playlist-song/<int:song_id>/', 
         views.add_playlist_song, 
         name='add-playlist-song'
         ),
    path('playlist/<int:playlist_id>/remove-playlist-song/<int:song_id>/', 
         views.remove_playlist_song, 
         name='remove-playlist-song'
         ),
]