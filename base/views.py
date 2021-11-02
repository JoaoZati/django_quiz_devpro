from django.shortcuts import render, redirect

from base.forms import ParticipantForm
from base.models import Question, Participant
from django.urls import reverse # noqa


def home(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            participant = Participant.objects.get(email=email)
        except Participant.DoesNotExist:
            form = ParticipantForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/question/1')
            context = {'form': form}
            return render(request, 'base/index.html', context)
        request.session['participant_id'] = participant.id
        return redirect('/question/1')

    return render(request, 'base/index.html')


def questions(request, index):
    try:
        participant_id = request.session['participant_id']
    except KeyError:
        return redirect('/')
    question = Question.objects.filter(available=True).order_by('id')[index - 1]
    context = {
        'index_question': index,
        'question': question,
    }
    return render(request, 'base/game.html', context)


def ranking(request):
    return render(request, 'base/end.html')
