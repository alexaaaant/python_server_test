from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render

def popular_questions(request):
    page = request.GET.get('page','')
    questions = models.Question.objects.popular()
    limit = request.GET.get('limit', 2)
    page = request.GET.get('page', page)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'qa/popular_questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def question(request, id):
    question = get_object_or_404(models.Question, id=id)
    answers = models.Answer.objects.filter(question_id=id)[:]
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers
    })
