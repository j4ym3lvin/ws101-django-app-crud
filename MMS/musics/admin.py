from django.contrib import admin
from .models import Music

class MusicAdmin(admin.ModelAdmin):
    list_display = ('music_name', 'music_artist', 'music_genre')

admin.site.register(Music, MusicAdmin)
# Register your models here.
