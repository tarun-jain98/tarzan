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
<<<<<<< Updated upstream
<<<<<<< HEAD

=======
>>>>>>> 8875cd6a93047497d31a8fe9b13c1d23aae9d4ab
    url(r'^honours/', views.honours, name="honours"),
    url(r'^online_courses/', views.online_courses, name="online_courses"),
    url(r'^consultancy/', views.consultancy, name="consultancy"),
    url(r'^phd_guide/', views.phd_guide, name="phd_guide"),
    url(r'^phd_self/', views.phd_self, name="phd_self"),
    url(r'^conference_journal/', views.conference_journal, name="conference_journal"),
    url(r'^funded_projects/', views.funded_projects, name="funded_projects"),

<<<<<<< HEAD


=======
>>>>>>> 8875cd6a93047497d31a8fe9b13c1d23aae9d4ab
=======

>>>>>>> Stashed changes

]
