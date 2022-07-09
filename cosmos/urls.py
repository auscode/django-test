from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("harsh", views.harsh, name="my namae"),
    path("<str:name>", views.greet, name="greet")
]
