from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def index(request):
    landingPageDivs=[1,2,3]
    context={'landingPageDivs' : landingPageDivs}

    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        if email and password :
            user=user_list.objects.filter(email==email)
            print(user)
            return "hell"
            if user and user.password==password:
                if user.des=="Admin":
                    redirect("/admin_home")
            

    return render(request,'index.html', context)

def index2(requset):
    opts=Gen_op.objects.all
    context ={'opts' : opts}


    if requset.method == 'POST':
        C_password = requset.POST['ConfirmPassword']
        username=requset.POST['Username']
        gender=requset.POST['Gender']
        age=requset.POST['Age']
        password=requset.POST['Password']
        
        # if password==C_password:
        #     if Credentials.objects.filter(username=username).exists():
        #         messages.info(requset, 'Username already in use\nTry logging in')
                
        #         return redirect('index')
        #     else:
        #         user=Credentials.objects.create(username=username,gender=gender,age=age,password=password)
        #         user.save()
        #         # redirecting left
        # else:
        #     messages.info(requset, 'Password and confirm password dosent match')
            
            # return redirect('index')
    
    return render(requset,'index2.html', context)

def counter(request):
    text = request.POST['text']
    context={}

    context['no_of_words']=len(text.split())
    print(context)

    return render(request, 'counter.html', context)

def admin_home(request):
    return render(request,'admin_home.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')