from django.shortcuts import render

from base.models import Question


def home(request):
    return render(request, 'base/index.html')


def questions(request, index):
    question = Question.objects.filter(available=True).order_by('id')[index - 1]
    context = {
        'index_question': index,
        'question': question,
    }
    return render(request, 'base/game.html', context)


def ranking(request):
    return render(request, 'base/end.html')
