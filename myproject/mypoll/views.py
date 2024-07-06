from django.shortcuts import render
from django.http import HttpResponse, Http404
# from .models import Question
# from django.template import loader


# Create your views here.
def index(request):
    # 1.  we need to set models.py to get latest_question_list
    # 2. after that:
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {'latest_question_list': 'Null'}

    return render(request, template, context)

def results(request, question_id):
    return HttpResponse("You're looking at results of question %s." % question_id)

def detail(request, question_id):
    # 1. we need models.py to make this code work
    # try:
    #     question = Question.obejcts.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question Dosnt Exist')
    return render(request, 'polls/detail.html', {'question': question_id})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)