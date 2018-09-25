from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404


def index(request):

    context = { 'info': "Hola" }
    return render(request, 'info/index.html', context)