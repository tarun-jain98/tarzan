from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import modelformset_factory

class LoginForm(AuthenticationForm):
	'''
	Form for taking Username and password
	'''
	username = forms.CharField(label="username", max_length=30,
							   widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'id': 'username','placeholder': 'Enter Username'}))
	password = forms.CharField(label="Password", max_length=30,
							   widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'otp', 'id': 'otp', 'placeholder': 'Enter OTP'}))


# class form_test_year(forms.ModelForm):
# 	class Meta:
# 		model = test_year
# 		fields = '__all__'


class form_fdp(forms.ModelForm):
	class Meta:
		model = fdp
		fields = '__all__'
		exclude = ['info','year']


class form_refreshers_course(forms.ModelForm):
	class Meta:
		model = refreshers_course
		fields = '__all__'
		exclude = ['info','year']


class form_sttp(forms.ModelForm):
	class Meta:
		model = sttp
		fields = '__all__'
		exclude = ['info','year']


class form_interaction(forms.ModelForm):
	class Meta:
		model = interaction
		fields = '__all__'
		exclude = ['info','year']


class form_open_courses(forms.ModelForm):
	class Meta:
		model = open_courses
		fields = '__all__'
		exclude = ['info','year']

class form_honours(forms.ModelForm):
	class Meta:
		model = honours
		fields = '__all__'
		exclude = ['info','year']

class form_online_courses(forms.ModelForm):
	class Meta:
		model = online_courses
		fields = '__all__'
		exclude = ['info','year']

class form_counsltancy(forms.ModelForm):
	class Meta:
		model = counsltancy
		fields = '__all__'
		exclude = ['info','year']


class form_funding(forms.ModelForm):
	class Meta:
		model = funding
		fields = '__all__'
		exclude = ['info','year']

class form_exclusive_research(forms.ModelForm):
	class Meta:
		model = exclusive_research
		fields = '__all__'
		exclude = ['info','year']


class form_conference_journal(forms.ModelForm):
	class Meta:
		model = conference_journal
		fields = '__all__'
		exclude = ['info','year']

class form_book(forms.ModelForm):
	class Meta:
		model = book
		fields = '__all__'
		exclude = ['info','year']

class form_phd_guide(forms.ModelForm):
	class Meta:
		model = phd_guide
		fields = '__all__'
		exclude = ['info','year']


class form_phd_self(forms.ModelForm):
	class Meta:
		model = phd_self
		fields = '__all__'
		exclude = ['info','year']


class form_open_courses(forms.ModelForm):
	class Meta:
		model = open_courses
		fields = '__all__'
		exclude = ['info','year']



class form_exclusive_research(forms.ModelForm):
	class Meta:
		model = exclusive_research
		fields = '__all__'
		exclude = ['info','year']
