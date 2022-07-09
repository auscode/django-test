from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django import forms


class NewTaskForms(forms.Form):
    task = forms.CharField(label="NewTask")

# Create your views here.


def index(request):
    if "task" not in request.session:
        request.session["task"] = []
    return render(request, "task/index.html", {
        "task": request.session["task"]
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForms(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["task"] += [task]
            return HttpResponseRedirect(reverse("task:index"))

        else:
            return render(request, "task/add.html", {
                "form": form
            })
    return render(request, "task/add.html", {
        "form": NewTaskForms()
    })
