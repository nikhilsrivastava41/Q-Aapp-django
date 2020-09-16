from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .models import People
from .models import AnswerQuestion
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['password']
        user = User.objects.create_user(
            username=uname, first_name=fname, last_name=lname, password=password)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            print(False)
            return redirect("login")
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def queslist(request):
    queslist = Question.objects.all()
    return render(request, 'queslist.html', {'queslist': queslist})


def quesdetail(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'quesdetail.html', {'ques': question})


def ansdetail(request, id):
    if request.method == 'POST':
        a = request.POST['a']
        num = id
        ans = AnswerQuestion(a=a, num=id)
        print(num + " " + a)
        ans.save()
        return redirect('/')
    else:
        question = Question.objects.get(id=id)
        return render(request, 'ansdetail.html', {'ques': question})


def quesans(request):
    return render(request, 'quesans.html')


def askques(request):
    if request.method == 'POST':
        q = request.POST['q']
        title = request.POST['title']
        ques = Question()
        ques.title = title
        ques.q = q
        ques.save()
        return redirect('/')
    else:
        return render(request, 'askques.html')
