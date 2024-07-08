from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# from django.template import loader


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {'latest_question_list': latest_question_list}

    return render(request, template, context)

def results(request, question_id):
    return HttpResponse("You're looking at results of question %s." % question_id)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question Dosnt Exist')

    # 2. Better way to use 404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)