from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "cosmos/index.html")


def harsh(request):
    return HttpResponse("my name is harshit")


def greet(request, name):
    return render(request, "cosmos/greet.html", {
        "name": name.capitalize()
    })
