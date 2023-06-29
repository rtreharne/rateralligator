from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewAlligatorForm

def index(request):
    return render(request, "core/index.html")

def create(request):
    form = NewAlligatorForm()

    return render(request, "core/create.html", {"form": form})

