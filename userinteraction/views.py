from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def userinteraction(request):
    return HttpResponse("<h1>hey i django server.</h1>")