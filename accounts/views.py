from django.shortcuts import render, HttpResponse

# Create your views here.


def signin(request):
    return HttpResponse("Signin Page")


def signup(request):
    return HttpResponse("Signup Page")