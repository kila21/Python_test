from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    # 1.  we need to set models.py to get latest_question_list
    # 2. after that:
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': 'Null'}
    
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    return HttpResponse("You're looking at results of question %s." % question_id)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)