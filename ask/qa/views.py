from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request, id):
    question = get_object_or_404(models.Question, id=id)
    answers = models.Answer.objects.filter(question_id=id)[:]
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers
    })
