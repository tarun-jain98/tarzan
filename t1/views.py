from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . import forms

# Create your views here.


def fdp(request):
    form = forms.form_fdp()
    return render(request,'fdp.html',{'form':form})

def ref_course(request):
    form = forms.form_refreshers_course()
    return render(request,'ref_course.html',{'form':form})

def sttp(request):
    form = forms.form_sttp()
    return render(request,'sttp.html',{'form':form})

def book(request):
    form = forms.form_book()
    return render(request,'book.html',{'form':form})

def interaction(request):
    form = forms.form_interaction()
    return render(request,'interaction.html',{'form':form})

def honours(request):
    form = forms.form_honours()
    return render(request,'honours.html',{'form':form})
