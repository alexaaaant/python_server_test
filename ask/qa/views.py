from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def new_questions(request):
    page = request.GET.get('page', 1)
    questions = models.Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', page)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })


def popular_questions(request):
    page = request.GET.get('page', 1)
    questions = models.Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', page)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'qa/questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })


def question(request, id):
    if request.method == "POST":
        d = request.POST.copy()
        d["question"] = id
        form = forms.AnswerForm(d)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        question = get_object_or_404(models.Question, id=id)
        answers = models.Answer.objects.filter(question_id=id)[:]
        return render(request, 'qa/question.html', {
            'question': question,
            'answers': answers
        })


def ask(request):
    if request.method == "POST":
        form = forms.AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect(q.get_url())
    return render(request, 'qa/ask.html')
