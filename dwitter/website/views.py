from django.shortcuts import render
from django.http import HttpResponse


def timeline(request):
    return HttpResponse('Welcome to dwitter!')
