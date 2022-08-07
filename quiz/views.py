from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'POST':
        # print(request.POST)
        questions = QuesModel.objects.all()
        correct = 0
        total = 0

        for q in questions:
            # print(request.POST.get(q.question))
            # print(q.ans)
            total+=1
            if q.ans ==  request.POST.get(q.question):
                correct+=1

        
        # print(score)
        username = request.POST.get('name')
        email = request.POST.get('email')

        Score.objects.create(username=username, email=email, correct=correct, total_questions = total)
        return render(request,'thanx.html')
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home.html',context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'register.html',context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('addQuestion')
       context={}
       return render(request,'login.html',context)


def addQuestion(request):
    if request.user.is_authenticated:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('addQuestion')
        context={'form':form}
        return render(request,'addQuestion.html',context)
    else: 
        return redirect('login') 

def logout(request):
    auth.logout(request)
    return redirect('/')

def thanx(request):
    return render(request, 'thanx')
