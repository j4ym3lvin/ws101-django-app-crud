
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('musics/', views.musics, name='musics'),
    path('musics/details/<int:id>/', views.details, name='details'),
    path('musics/create/', views.create_music, name='create_music'),
    path('musics/edit/<int:id>/', views.edit_music, name='edit_music'),  # Add this line
    path('musics/delete/<int:id>/', views.delete_music, name='delete_music'),  # Add this line
    path('testing/', views.testing, name='testing'),
]