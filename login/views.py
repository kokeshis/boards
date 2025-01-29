from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import MyForm


from django.contrib.auth import login


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login:login")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})

def index(request):
    return HttpResponse("Hello Django")
