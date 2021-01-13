from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse("Hello World")
    return render (request, 'quiz/index.html')

def game(request, id):
    context = {'id' : id}
    #return HttpResponse("Hello World")
    return render (request, 'quiz/game.html')

def score(request):
    #return HttpResponse("Hello World")
    return render (request, 'quiz/score.html')