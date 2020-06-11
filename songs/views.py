
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,MySongs
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout , authenticate
from .forms import CreateForm

def home(request):
    projects = Project.objects.all()
    return render(request,'songs/home.html',{'projects':projects})



def sangeet(request):
    return render(request,'songs/sangeet.html')

def mymusic(request):
    music = MySongs.objects.filter(user=request.user)
    return render(request,'songs/mymusic.html',{'music':music})

def signupuser(request):
    if request.method == 'GET':
        return render(request,'songs/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('mymusic')

            except IntegrityError:
                return render(request,'songs/signupuser.html',{'form':UserCreationForm(),'error':'Please Choose a different Username.This one is already taken'})
        else :
            return render(request,'songs/signupuser.html',{'form':UserCreationForm(),'error':'Password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'songs/loginuser.html',{'form':AuthenticationForm()})
    else :
        user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request,'songs/loginuser.html',{'form':AuthenticationForm(),'error':'username and password doesnot match.'})
        else:
            login(request, user)
            return redirect('mymusic')

def createmysongs(request):
    if request.method == 'GET':
        return render(request,'songs/createmysongs.html',{'form':CreateForm()})
    else:
        try:
            form = CreateForm(request.POST)
            newmysong = form.save(commit=False)
            newmysong.user = request.user
            newmysong.save()
            return redirect('mymusic')
        except ValueError:
            return render(request,'songs/createmysongs.html',{'form':CreateForm(),'error':'Bad Data passed in. Try Again'})

def logoutuser(request):
       if request.method == 'POST':
           logout(request)
           return redirect('home')
