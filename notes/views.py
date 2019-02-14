from django.shortcuts import render, HttpResponse

# Create your views here.

def create(request):
    return HttpResponse("Create New Post")


def delete(request):
    return HttpResponse("Deleting a post")