from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from . import forms

app_name = 't1'

urlpatterns = [

    url(r'^fdp/', views.fdp, name="fdp"),
    url(r'^ref_course/', views.ref_course, name="ref_course"),
    url(r'^sttp/', views.sttp, name="sttp"),
    url(r'^book/', views.book, name="book"),
    url(r'^interaction/', views.interaction, name="interaction"),


]
