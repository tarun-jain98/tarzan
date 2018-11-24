from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . import forms

# Create your views here.


def fdp(request):
    form = forms.form_fdp()
    return render(request,'fdp.html',{'form':form})

def ref_course(request):
    return render(request,'ref_course.html')

def sttp(request):
    return render(request,'sttp.html')

def book(request):
    return render(request,'book.html')

def interaction(request):
    return render(request,'interaction.html')
