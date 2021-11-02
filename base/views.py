from django.shortcuts import render, redirect

from base.forms import ParticipantForm
from base.models import Question, Participant, Answer
from django.urls import reverse  # noqa


def home(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            participant = Participant.objects.get(email=email)
        except Participant.DoesNotExist:
            form = ParticipantForm(request.POST)
            if form.is_valid():
                form.save()
                participant = Participant.objects.get(email=email)
                request.session['participant_id'] = participant.id
                return redirect('/question/1')
            context = {'form': form}
            return render(request, 'base/index.html', context)
        request.session['participant_id'] = participant.id
        return redirect('/ranking/')

    return render(request, 'base/index.html')


MAX_SCORE = 3


def questions(request, index):
    global MAX_SCORE

    try:
        participant_id = request.session['participant_id']
    except KeyError:
        return redirect('/')

    try:
        question = Question.objects.filter(available=True).order_by('id')[index - 1]
    except IndexError:
        return redirect('/ranking/')
    context = {
        'index_question': index,
        'question': question,
    }

    if request.method == 'POST':
        index_answer = int(request.POST['answer_index'])
        if index_answer == question.right_answer:
            try:
                Answer(participant_id=participant_id, question=question, points=MAX_SCORE).save()
            except Exception:
                return redirect(f'/question/{index + 1}')
            MAX_SCORE = 3
            return redirect(f'/question/{index + 1}')
        context['index_answer'] = index_answer
        MAX_SCORE = max(0, MAX_SCORE - 1)

    return render(request, 'base/game.html', context)


def ranking(request):
    return render(request, 'base/end.html')
