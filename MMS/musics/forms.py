# forms.py
from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['music_id', 'music_name', 'music_artist', 'music_genre'] 