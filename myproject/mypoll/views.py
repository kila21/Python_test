from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reques):
    return HttpResponse('This is Poll!')

def results(request, question_id):
    return HttpResponse("You're looking at results of question %s." % question_id)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)