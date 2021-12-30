from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    # return HttpResponse("Hello Welcome to Django") for diaplaying strings
    return render(request, 'key/home.html', {'key': 'Random Generated AE$#$%SDRT'})


def key_display(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%^&*()_+=-{}|[]\:;"><.,/?~`'))

    length = int(request.GET.get('length'))  # length variable get from the home.html file
    key = ''
    for x in range(length):
        key += random.choice(characters)

    return render(request, 'key/key_display.html', {'key': key})
