from django.shortcuts import render,redirect
from .models import *
from .models import Receipe
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def receipes(request):# taking data from frontend to backend 
    if request.method =="POST":
       data =request.POST  #data put leta h bss text 
       receipe_name=data.get('receipe_name')#data text
       receipe_discription=data.get('receipe_discription')
       receipe_image=request.FILES.get('receipe_image')#onli takes images 

       Receipe.objects.create(
           receipe_name=receipe_name,
           receipe_discription=receipe_discription,
           receipe_image=receipe_image
             )

       return redirect('/receipes/')# alert nhi dega 
    
    
    queryset=Receipe.objects.all()
    
    if request.GET.get('search'):
       queryset=queryset.filter(receipe_name__icontains= request.GET.get('search'))# icontains search karega ki ye string ati h ki nahi is particcular strings mai ki nahi 

       
    
    
    context={'receipes':queryset}
    return render(request,'receipes.html',context)

def delete_receipe(request,id):
  queryset=Receipe.objects.get(id=id)
  queryset.delete()
  return redirect('/receipes/')


def update_receipe(request,id):
   queryset=Receipe.objects.get(id = id)
   
   
   if request.method == "POST":
      data =request.POST

      receipe_name=data.get('receipe_name')
      receipe_description=data.get('receipe_description')
      receipe_image=request.FILES.get('receipe_image')

      queryset.receipe_name = receipe_name
      queryset.receipe_discription = receipe_description

      if receipe_image:
         queryset.receipe_image=receipe_image
      queryset.save()
      return redirect('/receipes/')

      
   context={'receipe':queryset}
   return render(request,'update_receipes.html',context)


def login_page(request):
   if request.method=="POST":
      email=request.POST.get('email')
      password = request.POST.get('password')

      # if not  User.objects.filter(username=username).exists():
      #    messages.error(request,'Invalid username')
      #    return redirect('/login/')

      try:
         user_obj=User.objects.get(email=email)
         username=user_obj.username

      except User.DoesNotExist:
         messages.error(request,'User not found')
         return redirect('/login/')

      user =authenticate(username=username,password=password)
      if user is None:
         messages.error(request,'Invalid password')
         return redirect('/login/')
         
      else:
         login(request,user)
         next_url=request.GET.get('next')
         if next_url:
            return redirect(next_url)
         return redirect('/receipes/')
         
   return render (request,'login.html')
 
def logout_page(request):
   logout(request)
   return redirect ('/login/')

def register(request):
   if request.method == "POST":
      username= request.POST.get('username')
      email= request.POST.get('email')
      password= request.POST.get('password')


      user= User.objects.filter(username = username)

      if user.exists():
          
          messages.info(request,'full name already taken')
          return redirect("/login/")

      user =User.objects.create(
        username = username ,
        email=email     
             )
      
      user.set_password(password)
      user.save()

      messages.info(request,'account created successfully')

      return redirect('/register/')
   return render (request,'register.html')

