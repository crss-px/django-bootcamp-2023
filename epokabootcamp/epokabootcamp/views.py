from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def hello_world(request):
    registered_users = [
        {"name": "Kristjan", "surname": "Pashollari"},
        {"name": "Enes", "surname": "Bytyqi"},
        {"name": "Igli", "surname": "Zeneli"},
        {"name": "Admirim", "surname": "Kasolli"}
    ]
    context = {
        'registered_users': registered_users
    }
    return render(request, "index.html", context)

def second_function(request):
    return HttpResponse("This is another function!")