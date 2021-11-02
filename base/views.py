from django.shortcuts import render


def home(request):
    return render(request, 'base/index.html')


def questions(request, indice):
    return render(request, 'base/game.html')
