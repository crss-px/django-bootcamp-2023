from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World!")

def second_function(request):
    return HttpResponse("This is another function!")