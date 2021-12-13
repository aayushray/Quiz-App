from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def home(request):
    
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        for q in questions:
            print(request.POST.get(q.question))
            print(q.ans)
            print()
        # context = {
        #     'score':score,
        #     'correct':correct,
        #     'wrong':wrong,
        #     'percent':percent,
        #     'total':total
        # }
        return render(request,'thanx.html')
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home.html',context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password doesnt match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('addQuestion')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def addQuestion(request):
    if request.user.is_staff:
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