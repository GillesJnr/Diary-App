from django.shortcuts import render, HttpResponse

# Create your views here.


def create(request):
    return render(request, "notes/base.html")


def update(request, id):
    return HttpResponse("Update Post")


def delete(request):
    return HttpResponse("Deleting a post")
