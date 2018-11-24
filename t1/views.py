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
<<<<<<< HEAD

=======
>>>>>>> 8875cd6a93047497d31a8fe9b13c1d23aae9d4ab
    form = forms.form_book()
    return render(request,'book.html',{'form':form})

def interaction(request):
    form = forms.form_interaction()
    return render(request,'interaction.html',{'form':form})

def honours(request):
    form = forms.form_honours()
    return render(request,'honours.html',{'form':form})

def online_courses(request):
    form = forms.form_online_courses()
    return render(request,'online_courses.html',{'form':form})

def consultancy(request):
    form = forms.form_counsltancy()
    return render(request,'consultancy.html',{'form':form})

def phd_guide(request):
    form = forms.form_phd_guide()
    return render(request,'phd_guide.html',{'form':form})

def phd_self(request):
    form = forms.form_phd_self()
    return render(request,'phd_self.html',{'form':form})

def phd_self(request):
    form = forms.form_phd_self()
    return render(request,'phd_self.html',{'form':form})

def conference_journal(request):
    form = forms.form_conference_journal()
    return render(request,'conference_journal.html',{'form':form})

def funded_projects(request):
    form = forms.form_funding()
    return render(request,'funded_projects.html',{'form':form})
<<<<<<< HEAD
=======

>>>>>>> 8875cd6a93047497d31a8fe9b13c1d23aae9d4ab
