from django.shortcuts import render
from django.http import HttpResponse
from .models import Poetry

def all_poetry(request):

    poetrys = Poetry.objects.all()
    return render(request,'poetry/all_poetry.html',{'poetrys':poetrys})

def detailp(request):

    return render(request,'poetry/detailp.html')
