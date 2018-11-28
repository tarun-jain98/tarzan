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
    


    url(r'^fdp/(?P<year>[\w\-]+)$',views.fdp1,name="fdp1"),

    url(r'^ref_course/(?P<year>[\w\-]+)$',views.ref_course1,name="ref_course1"),

    url(r'^sttp/(?P<year>[\w\-]+)$',views.sttp1,name="sttp1"),

    url(r'^book/(?P<year>[\w\-]+)$',views.book1,name="book1"),

    url(r'^interaction/(?P<year>[\w\-]+)$',views.interaction1,name="interaction1"),

    url(r'^honours/(?P<year>[\w\-]+)$',views.honours1,name="honours1"),

    url(r'^online_courses/(?P<year>[\w\-]+)$',views.online_courses1,name="online_courses1"),

    url(r'^consultancy/(?P<year>[\w\-]+)$',views.consultancy1,name="consultancy1"),

    url(r'^phd_guide/(?P<year>[\w\-]+)$',views.phd_guide1,name="phd_guide1"),

    url(r'^phd_self/(?P<year>[\w\-]+)$',views.phd_self1,name="phd_self1"),

    url(r'^conference_journal/(?P<year>[\w\-]+)$',views.conference_journal1,name="conference_journal1"),

    url(r'^funded_projects/(?P<year>[\w\-]+)$',views.funded_projects1,name="funded_projects1"),

    url(r'^open_courses/(?P<year>[\w\-]+)$',views.open_courses1,name="open_courses1"),

    url(r'^exclusive_research/(?P<year>[\w\-]+)$',views.ex_research1,name="ex_research1"),








# preview


    url(r'^preview_fdp/(?P<year>[\w\-]+)$',views.fdp1_preview,name="fdp1_preview"),

    url(r'^preview_ref_course/(?P<year>[\w\-]+)$',views.ref_course1_preview,name="ref_course1_preview"),

    url(r'^preview_sttp/(?P<year>[\w\-]+)$',views.sttp1_preview,name="sttp1_preview"),

    url(r'^preview_book/(?P<year>[\w\-]+)$',views.book1_preview,name="book1_preview"),

    url(r'^interaction/(?P<year>[\w\-]+)$',views.interaction1_preview,name="interaction1_preview"),

    url(r'^honours/(?P<year>[\w\-]+)$',views.honours1_preview,name="honours1_preview"),

    url(r'^online_courses/(?P<year>[\w\-]+)$',views.online_courses1_preview,name="online_courses1_preview"),

    url(r'^consultancy/(?P<year>[\w\-]+)$',views.consultancy1_preview,name="consultancy1_preview"),

    url(r'^phd_guide/(?P<year>[\w\-]+)$',views.phd_guide1_preview,name="phd_guide1_preview"),

    url(r'^phd_self/(?P<year>[\w\-]+)$',views.phd_self1_preview,name="phd_self1_preview"),

    url(r'^conference_journal/(?P<year>[\w\-]+)$',views.conference_journal1_preview,name="conference_journal1_preview"),

    url(r'^funded_projects/(?P<year>[\w\-]+)$',views.funded_projects1_preview,name="funded_projects1_preview"),

    url(r'^open_courses/(?P<year>[\w\-]+)$',views.open_courses1_preview,name="open_courses1_preview"),

    url(r'^exclusive_research/(?P<year>[\w\-]+)$',views.oexclusive_research1_preview,name="exclusive_research1_preview"),
    



















    







]
