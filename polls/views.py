from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from polls.forms import AnswerForm
from polls.models import Poll, UserPollResult, Question, Answer


def index(request):
    if request.user.is_authenticated:
        polls = Poll.objects.exclude(
            id__in=(UserPollResult.objects.filter(
                user=request.user).values('poll')))
    else:
        polls = Poll.objects.all()
    context = {'polls': polls}
    template = 'polls/index.html'
    return render(request, template, context)


@login_required
def polling(request, poll_id, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = AnswerForm(question)
    template = 'polls/question.html'
    context = {
        'form': form,
        'question': question,
        'poll_id': poll_id,
    }
    if request.POST.getlist('answers'):
        up_score(request, poll_id)

    if not question.next:
        context['finish'] = True

    return render(request, template, context)


def finish(request, poll_id):
    result = up_score(request, poll_id)
    template = 'polls/finish.html'
    poll = Poll.objects.get(id=poll_id)
    context = {
        'poll': poll,
        'result': result,

    }
    user = request.user
    user.money += result.correct_answer
    user.save()
    return render(request, template, context)


def up_score(request, poll_id):
    answer = request.POST.get('answers')
    result, status = UserPollResult.objects.get_or_create(
        user=request.user, poll_id=poll_id
    )
    result.done += 1

    if Answer.objects.get(id=int(answer)).correct:
        result.correct_answer += 1

    result.save()
    return result
