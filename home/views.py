from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples=[
        {'name':'harsh','age':20},
        {'name':'seejal','age':10},
        {'name':'shorya','age':15},
        {'name':'ak','age':17},
        {'name':'balla','age':22},
        {'name':'harshita','age':20},
    ]
    
    for people in peoples:
        print(people)
    
    
    return render(request,"home/index.html",context={'peoples':peoples})


def about(request):
    return HttpResponse("""
        <h1>hello harsh </h1>""")

    
