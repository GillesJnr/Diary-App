from django.shortcuts import render, HttpResponse
from .forms import NoteForm

# Create your views here.


def create(request):
    form = NoteForm()
    return render(request, "notes/index.html", {'form': form})


def update(request, id):
    return HttpResponse("Update Post")


def delete(request):
    return HttpResponse("Deleting a post")
