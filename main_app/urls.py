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
]