from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def fdp(request):
    return render(request,'fdp.html')

def ref_course(request):
    return render(request,'ref_course.html')

def sttp(request):
    return render(request,'sttp.html')

def book(request):
    return render(request,'book.html')
