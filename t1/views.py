from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . import forms
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.




def login(request):
    if(request.method=='POST'):

        userna = request.POST.get('username')
        username = userna.upper()

        if(User.objects.filter(username=username).exists()):
            user = User.objects.get(username=username)
            first_name = user.first_name
            email = user.email
            phone = user.phone
            # random_otp = r''.join(random.choice('0123456789') for i in range(4))
            # phone_otp(random_otp,phone)

            random_otp = '1234'

            hashed_pwd = make_password(random_otp)
            User.objects.filter(username=username).update(password=hashed_pwd)

            return HttpResponseRedirect("/login/user=" + username)

    return render(request,'login.html')

def index(request):

    # form1 = forms.form_test_year()

   

    data0 = User.objects.get(username=request.user)
    print(data0.department)

    data1 = Field.objects.all()
    data2 = Year.objects.all()
    data3 = zip(data1,data2)

   


    context = {
            'data0':data0,
            'data1':data1,
            'data2':data2,
            'data3':data3,
            
            
        }

    return render(request,'index.html',context = context)


def decide_view(request):
    if request.user.is_assistant_professor():
        return HttpResponseRedirect("/index/")
       
    elif request.user.is_associate_professor():
        return HttpResponseRedirect("/index/")
        

    elif request.user.is_professor():
        return HttpResponseRedirect("/index/")
        

    elif request.user.is_hod():
        print("ASS")
       

    elif request.user.is_principal():
        print("ASS")
       

    elif request.user.is_ao():
        print("AO")
        




def fdp1(request,year):
    form = forms.form_fdp()


    if fdp.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_fdp/'+year)

    
    if request.method == 'POST':
        # status = User.objects.get(username=request.user)
        form = forms.form_fdp(request.POST)


        if form.is_valid():
            print(year)
            
            obj = form.save(commit=False)
            obj.info = request.user
            obj.year = year

            obj.save()

            return HttpResponseRedirect('/index')

    return render(request,'fdp.html',{'form':form})


def fdp1_preview(request,year):


    data1 = fdp.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_fdp.html',context=context)







def ref_course1(request,year):
    form = forms.form_refreshers_course()
    if ref_course.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_ref_course/'+year)

    if request.method == 'POST':

        form = forms.form_refreshers_course(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user
            obj.year = year

            obj.save()

            return HttpResponseRedirect('/index')

    return render(request,'ref_course.html',{'form':form})



def ref_course1_preview(request,year):


    data1 = ref_course.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_ref_course.html',context=context)




def sttp1(request,year):
    form = forms.form_sttp()
    if sttp.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_sttp/'+year)
    
    if request.method == 'POST':


        form = forms.form_sttp(request.POST)


        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')


    return render(request,'sttp.html',{'form':form})


def sttp1_preview(request,year):


    data1 = sttp.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_sttp.html',context=context)    



def book1(request,year):
    form = forms.form_book()
    if book.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_book/'+year)
    if request.method == 'POST':

        form = forms.form_book(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')

    return render(request,'book.html',{'form':form})

def book1_preview(request,year):


    data1 = book.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_book.html',context=context) 



def interaction1(request,year):
    form = forms.form_interaction()
    if interaction.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_interaction/'+year)

    if request.method == 'POST':

        form = forms.form_interaction(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')

    return render(request,'interaction.html',{'form':form})


def interaction1_preview(request,year):


    data1 = interaction.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_interaction.html',context=context)     



def honours1(request,year):
    form = forms.form_honours()
    if honours.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_honours/'+year)
    if request.method == 'POST':

        form = forms.form_honours(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')



    return render(request,'honours.html',{'form':form})

def honours1_preview(request,year):


    data1 = honours.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_honours.html',context=context) 


def online_courses1(request,year):
    form = forms.form_online_courses()
    if online_courses.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_online_courses/'+year)
    if request.method == 'POST':

        form = forms.form_online_courses(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')

    return render(request,'online_courses.html',{'form':form})

def online_courses1_preview(request,year):
    data1 = online_courses.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_online_courses.html',context=context) 


def consultancy1(request,year):
    form = forms.form_counsltancy()
    if consultancy.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_consultancy/'+year)
    if request.method == 'POST':

        form = forms.form_counsltancy(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')



    return render(request,'consultancy.html',{'form':form})

def consultancy1_preview(request,year):
    data1 = consultancy.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_consultancy.html',context=context) 

def phd_guide1(request,year):
    form = forms.form_phd_guide()
    if phd_guide.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_phd_guide/'+year)
    if request.method == 'POST':

        form = forms.form_phd_guide(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')

    return render(request,'phd_guide.html',{'form':form})

def phd_guide1_preview(request,year):
    data1 = phd_guide.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_phd_guide.html',context=context) 

def phd_self1(request,year):
    form = forms.form_phd_self()
    if phd_self.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_phd_self/'+year)
    if request.method == 'POST':

        form = forms.form_phd_self(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')

    return render(request,'phd_self.html',{'form':form})

def phd_self1_preview(request,year):
    data1 = phd_self.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_phd_self.html',context=context) 

def conference_journal1(request,year):
    form = forms.form_conference_journal()
    if conference_journal.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_conference_journal/'+year)
    if request.method == 'POST':

        form = forms.form_conference_journal(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')

    return render(request,'conference_journal.html',{'form':form})


def conference_journal1_preview(request,year):
    data1 = conference_journal.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_conference_journal.html',context=context)


def funded_projects1(request,year):
    form = forms.form_funding()
    if funded_projects.objects.filter(info=request.user).filter(year=year):
        
        return HttpResponseRedirect('/preview_funded_projects/'+year)
    if request.method == 'POST':

        form = forms.form_funding(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.info = request.user

            obj.save()

            return HttpResponseRedirect('/index')
    return render(request,'funded_projects.html',{'form':form})


def funded_projects1_preview(request,year):
    data1 = funded_projects.objects.filter(info=request.user).get(year=year)
    context={
            'key':data1
        }
    print(data1)
    return render(request,'preview_funded_projects.html',context=context)
