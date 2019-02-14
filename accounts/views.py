from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.


def login(request):
    return HttpResponse("Login Page")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, f'Account successfully created')
        return redirect("create")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def logout(request):
    return HttpResponse("Logout Page")


def profile(request):
    return HttpResponse("Profile Page")
