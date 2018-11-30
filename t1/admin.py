from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

admin.site.site_header = "Tarzan System";

admin.site.register(Designation)

admin.site.register(Department)
admin.site.register(Field)
admin.site.register(Year)

admin.site.register(author_type)
admin.site.register(agency_type)
admin.site.register(consultancy_type)
admin.site.register(investigator_type)


admin.site.register(index_type)

admin.site.register(int_ext)

admin.site.register(status)
admin.site.register(support)
admin.site.register(skills)


class UserResource(resources.ModelResource):
	class Meta:
		model = User


@admin.register(User)
class UserAdmin(DjangoUserAdmin, ImportExportModelAdmin):

	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'department','info')}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   )}),

		(('Status'), {'fields': ('teach_status',)}),

		(('Designation'), {'fields': ('designation',)}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
	search_fields = ('email', 'first_name', 'last_name', 'username', 'phone')
	ordering = ('username',)
	read_only = "password"
	resource_class = UserResource


class fdP(resources.ModelResource):
	class Meta:
		model = fdp


@admin.register(fdp)
class Fdp(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = fdP

	def name(self, instance):
		return instance.info.first_name


class refreshers_coursE(resources.ModelResource):
	class Meta:
		model = refreshers_course


@admin.register(refreshers_course)
class Refreshers_course(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = refreshers_coursE

	def name(self, instance):
		return instance.info.first_name		


class sttP(resources.ModelResource):
	class Meta:
		model = sttp


@admin.register(sttp)
class Sttp(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = sttP

	def name(self, instance):
		return instance.info.first_name	


class workshoP(resources.ModelResource):
	class Meta:
		model = workshop


@admin.register(workshop)
class Workshop(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = workshoP

	def name(self, instance):
		return instance.info.first_name	



class seminaR(resources.ModelResource):
	class Meta:
		model = seminar


@admin.register(seminar)
class Seminar(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = seminaR

	def name(self, instance):
		return instance.info.first_name	


class technical_talK(resources.ModelResource):
	class Meta:
		model = technical_talk


@admin.register(technical_talk)
class Technical_talk(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = technical_talK

	def name(self, instance):
		return instance.info.first_name	


class session_chaiR(resources.ModelResource):
	class Meta:
		model = session_chair


@admin.register(session_chair)
class Session_chair(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = session_chaiR

	def name(self, instance):
		return instance.info.first_name	



class online_courseS(resources.ModelResource):
	class Meta:
		model = online_courses


@admin.register(online_courses)
class Online_courses(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = online_courseS

	def name(self, instance):
		return instance.info.first_name	


class honourS(resources.ModelResource):
	class Meta:
		model = honours


@admin.register(honours)
class Honours(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = honourS

	def name(self, instance):
		return instance.info.first_name	


class counsltancY(resources.ModelResource):
	class Meta:
		model = counsltancy


@admin.register(counsltancy)
class Counsltancy(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = counsltancY

	def name(self, instance):
		return instance.info.first_name


class fundinG(resources.ModelResource):
	class Meta:
		model = funding


@admin.register(funding)
class Funding(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = fundinG

	def name(self, instance):
		return instance.info.first_name


# class exclusive_researcH(resources.ModelResource):
# 	class Meta:
# 		model = exclusive_research


# @admin.register(exclusive_research)
# class Exclusive_research(ImportExportModelAdmin):


# 	list_display = ('name',)
# 	search_fields = ('info__first_name',)
# 	ordering = ('id',)
# 	resource_class = exclusive_researcH

# 	def name(self, instance):
# 		return instance.info.first_name	

class conferencE(resources.ModelResource):
	class Meta:
		model = conference


@admin.register(conference)
class Conference(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = conferencE

	def name(self, instance):
		return instance.info.first_name	

class journaL(resources.ModelResource):
	class Meta:
		model = journal


@admin.register(journal)
class Journal(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = journaL

	def name(self, instance):
		return instance.info.first_name	


class booK(resources.ModelResource):
	class Meta:
		model = book


@admin.register(book)
class Book(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = booK

	def name(self, instance):
		return instance.info.first_name	

class chapteR(resources.ModelResource):
	class Meta:
		model = chapter


@admin.register(chapter)
class Chapter(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = chapteR

	def name(self, instance):
		return instance.info.first_name	


class phd_guidE(resources.ModelResource):
	class Meta:
		model = phd_guide


@admin.register(phd_guide)
class Phd_guide(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = phd_guidE

	def name(self, instance):
		return instance.info.first_name		


class phd_selF(resources.ModelResource):
	class Meta:
		model = phd_self


@admin.register(phd_self)
class Phd_self(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = phd_selF

	def name(self, instance):
		return instance.info.first_name								



