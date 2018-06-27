from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  # Http404
import datetime
from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)

    # response = '<ul>'
    # for i in q:
    #     c = i.choice_set.all()
    #     response += str(i) + '<br><ul>'
    #
    #     for j in c:
    #         response += '<li>' + str(j) + '</li>'
    #     response += '</ul><br>'
    # response += '</ul>'


def date_time(request):
    return HttpResponse("Current date and time is " + str(datetime.datetime.now()))


def detail(request, question_id):
    quest = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {"question": quest, })


def results(request, question_id):
    return HttpResponse("You are looking at the result of question no " + str(question_id))


def vote(request, question_id):
    return HttpResponse("You are voting on question " + str(question_id))
