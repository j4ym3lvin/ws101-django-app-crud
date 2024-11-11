from django.template import loader
from django.http import HttpResponse
from .models import Music
from django.shortcuts import render, redirect
from .forms import MusicForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def musics(request):
    my_musics = Music.objects.all().values()
    template = loader.get_template('all_musics.html')
    context = {
        'my_musics':my_musics,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my_musics = Music.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_musics' : my_musics
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'musics':['Good Graces', 'Coincidence', 'Taste']
    }
    return HttpResponse(template.render(context, request))

def create_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musics')  # Redirect to the music list after saving
    else:
        form = MusicForm()
    
    context = {
        'form': form
    }
    return render(request, 'create_music.html', context)

def edit_music(request, id):
    music = get_object_or_404(Music, id=id)
    if request.method == 'POST':
        form = MusicForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect('musics')  # Redirect to the music list after saving
    else:
        form = MusicForm(instance=music)

    context = {
        'form': form,
        'music': music
    }
    return render(request, 'edit_music.html', context)

def delete_music(request, id):
    music = get_object_or_404(Music, id=id)
    if request.method == 'POST':
        music.delete()
        return HttpResponseRedirect(reverse('musics'))  # Redirect to the music list after deletion
    return render(request, 'confirm_delete.html', {'music': music})

