from django.shortcuts import render


def home(request):
    return render(request, 'base/index.html')


def questions(request, index):
    context = {
        'index_question': index,
    }
    return render(request, 'base/game.html', context)


def ranking(request):
    return render(request, 'base/end.html')
