from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . import forms

# Create your views here.





def fdp1(request):
    form = forms.form_fdp()
    if fdp.objects.filter(info = request.user).exists():

        data = fdp.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_fdp.html',context=context)

    else:
        if request.method == 'POST':
            # status = User.objects.get(username=request.user)
            form = forms.form_fdp(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')

                # if status.teach_status == False:
                #     status.teach_status = True
                #     status.save()
                #     return HttpResponseRedirect('/index')






    return render(request,'fdp.html',{'form':form})



def ref_course1(request):
    form = forms.form_refreshers_course()
    if refreshers_course.objects.filter(info = request.user).exists():

        data = refreshers_course.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_ref_course.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_refreshers_course(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')




    return render(request,'ref_course.html',{'form':form})

def sttp1(request):
    form = forms.form_sttp()

    if sttp.objects.filter(info = request.user).exists():

        data = sttp.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_sttp.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_sttp(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')


    return render(request,'sttp.html',{'form':form})



def book1(request):
    form = forms.form_book()
    if book.objects.filter(info = request.user).exists():

        data = book.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_book.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_book(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')

    return render(request,'book.html',{'form':form})



def interaction1(request):
    form = forms.form_interaction()

    if interaction.objects.filter(info = request.user).exists():

        data = interaction.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_interaction.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_interaction(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')

    return render(request,'interaction.html',{'form':form})



def honours1(request):
    form = forms.form_honours()

    if honours.objects.filter(info = request.user).exists():

        data = honours.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_honours.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_honours(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')



    return render(request,'honours.html',{'form':form})



def online_courses1(request):
    form = forms.form_online_courses()

    if online_courses.objects.filter(info = request.user).exists():

        data = online_courses.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_online_courses.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_online_courses(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')

    return render(request,'online_courses.html',{'form':form})



def consultancy1(request):
    form = forms.form_counsltancy()

    if counsltancy.objects.filter(info = request.user).exists():

        data = counsltancy.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_counsltancy.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_counsltancy(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')



    return render(request,'consultancy.html',{'form':form})



def phd_guide1(request):
    form = forms.form_phd_guide()

    if phd_guide.objects.filter(info = request.user).exists():

        data = phd_guide.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_phd_guide.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_phd_guide(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')

    return render(request,'phd_guide.html',{'form':form})



def phd_self1(request):
    form = forms.form_phd_self()

    if phd_self.objects.filter(info = request.user).exists():

        data = phd_self.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_phd_self.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_phd_self(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')

    return render(request,'phd_self.html',{'form':form})



def conference_journal1(request):
    form = forms.form_conference_journal()

    if conference_journal.objects.filter(info = request.user).exists():

        data = conference_journal.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_conference_journal.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_conference_journal(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')

    return render(request,'conference_journal.html',{'form':form})



def funded_projects1(request):
    form = forms.form_funding()

    if funding.objects.filter(info = request.user).exists():

        data = funding.objects.filter(info = request.user)
        context = {
            'key':data
        }
        return render(request,'preview_funded_projects.html',context=context)

    else:
        if request.method == 'POST':

            form = forms.form_funding(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.info = request.user

                obj.save()

                return HttpResponseRedirect('/index')
    return render(request,'funded_projects.html',{'form':form})
