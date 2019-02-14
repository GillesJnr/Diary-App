from django.shortcuts import render, HttpResponse, redirect
from .forms import NoteForm
from .models import Note
# Create your views here.


def create(request,id=0):
    notes = Note.objects.filter(status=1).order_by('-id')[:3]
    if request.method == "GET":
        if id == 0:
            form = NoteForm()
        else:
            text = Note.objects.get(pk=id)
            form = NoteForm(instance=text)
            return render(request, "notes/index.html", {'form': form})
        context = {
            'form': form,
            'notes': notes
        }
        return render(request, "notes/index.html", context)

    elif request.method == "POST":
        if id==0:
            form = NoteForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            text = Note.objects.get(pk=id)
            form = NoteForm(request.POST,instance=text)
            if form.is_valid():
                form.save()
        return redirect("create")


def delete(request, id):
    note = Note.objects.get(pk=id)
    note.delete()
    return redirect("create")
