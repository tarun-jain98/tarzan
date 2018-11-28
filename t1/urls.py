from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from . import forms

app_name = 't1'

urlpatterns = [

    url(r'^$', views.login, name="login-username-view"),
    url(r'^login/', login, {'template_name': 'otp.html','authentication_form': forms.LoginForm}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'success.html'}, name='logout'),
    url(r'^main/', views.decide_view, name="decide-view"),

    url(r'^index/', views.index, name="index"),
    

    # url(r'^fdp/', views.fdp1, name="fdp1"),

    url(r'^fdp/(?P<year>[\w\-]+)$',views.fdp1,name="fdp1"),

    url(r'^ref_course/(?P<year>[\w\-]+)$',views.ref_course1,name="ref_course1"),

    
    
    url(r'^sttp/', views.sttp1, name="sttp1"),
    url(r'^book/', views.book1, name="book1"),
    url(r'^interaction/', views.interaction1, name="interaction1"),

    url(r'^honours/', views.honours1, name="honours1"),
    url(r'^online_courses/', views.online_courses1, name="online_courses1"),
    url(r'^consultancy/', views.consultancy1, name="consultancy1"),
    url(r'^phd_guide/', views.phd_guide1, name="phd_guide1"),
    url(r'^phd_self/', views.phd_self1, name="phd_self1"),
    url(r'^conference_journal/', views.conference_journal1, name="conference_journal1"),
    url(r'^funded_projects/', views.funded_projects1, name="funded_projects1"),


]
