from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Testimonials

def all_testimonials(request):
    test = Testimonials.objects.all()

    return render (request,'testimonials/all_testimonials.html',{'test':test})


def detail(request,test_id):
    test = get_object_or_404(Testimonials,pk=test_id)
    return render (request,'testimonials/detail.html',{'test':test})
