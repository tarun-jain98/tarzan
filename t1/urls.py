from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from . import forms

app_name = 't1'

urlpatterns = [

    url(r'^fdp/', views.fdp1, name="fdp1"),
    url(r'^ref_course/', views.ref_course1, name="ref_course1"),
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
