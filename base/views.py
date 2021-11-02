from django.shortcuts import render, redirect

from base.forms import ParticipantForm
from base.models import Question
from django.urls import reverse # noqa


def home(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            return redirect('/questions/1')
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
