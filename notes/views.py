from django.shortcuts import render, HttpResponse, redirect
from .forms import NoteForm
from .models import Note
# Create your views here.


def create(request):
    form = NoteForm()
    notes = Note.objects.filter(status=1)
    if request.method == "GET":
        context = {
            'form': form,
            'notes': notes
        }
        return render(request, "notes/index.html", context)

    elif request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("create")


def update(request, id):
    return HttpResponse("Update Post")


def delete(request):
    return HttpResponse("Deleting a post")
