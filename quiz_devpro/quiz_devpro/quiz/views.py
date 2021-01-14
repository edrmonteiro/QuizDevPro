from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Game

# Create your views here.

def index(request):
    #return HttpResponse("Hello World")
    return render (request, 'quiz/index.html')

def game(request, id):
    question = Game.objects.filter(available=True).order_by('id')[id - 1]
    context = {'id' : id, 'question': question}
    #return HttpResponse("Hello World")
    return render (request, 'quiz/game.html')

def score(request):
    #return HttpResponse("Hello World")
    return render (request, 'quiz/score.html')