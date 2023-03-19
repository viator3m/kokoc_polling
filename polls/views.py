from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'polls/index.html'
    return render(request, template)
