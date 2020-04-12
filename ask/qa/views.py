from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK 200')

def login(request, *args, **kwargs):
    return HttpResponse('OK login page')

def question(request, *args, **kwargs):
    return HttpResponse('OK question page')