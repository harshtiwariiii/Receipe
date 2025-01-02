from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples=[
        {'name':'harsh','age':20},
        {'name':'seejal','age':40},
        {'name':'shorya','age':15},
        {'name':'ak','age':17},
        {'name':'balla','age':22},
        {'name':'harshita','age':20},
    ]
    vegetables=[
        'tomato','pineapple','redphp'
    ]
    for people in peoples:
        print(people)
    
    
    return render(request,"home/index.html",context={'peoples':peoples,'vegetables':vegetables,'page':'home'})


def about(request):
    context={'page':'about' }
    return render(request,"home/about.html")

def contact(request):
    context={'page':'contact' }
    return render(request,"home/contact.html")

    
