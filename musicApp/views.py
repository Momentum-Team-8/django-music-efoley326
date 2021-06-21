from django.forms.widgets import DateTimeInput
from django.shortcuts import render, redirect, get_object_or_404
from .models import mainForm
from .forms import mainForm

# Create your views here.


def list_albums(request):
    albums = musicApp.objects.all()
    return render(request, "albums/album_list.html",
                  {"albums": albums})


def add_album(request):
    if request.method == 'GET':
        form = mainForm()
    else:
        form = mainForm(data=request.POST)
        if form.is_valid():
            form.save()
            add_album.created_date = DateTimeInput()
            return redirect(to='album_list')

    return render(request, "albums/add_album.html", {"form": form})


def edit_album(request, pk):
    album = get_object_or_404(musicApp, pk=pk)
    if request.method == 'GET':
        form = mainForm(instance=album)
    else:
        form = mainForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='album_list')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })

def delete_album(request, pk):
    album = get_object_or_404(musicApp, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='album_list')


    return render(request, "albums/delete_album.html",
                  {"album": album})