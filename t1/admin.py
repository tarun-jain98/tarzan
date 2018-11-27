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

admin.site.register(yes_no)
admin.site.register(index_type)

admin.site.register(int_ext)

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


class interactioN(resources.ModelResource):
	class Meta:
		model = interaction


@admin.register(interaction)
class Interaction(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = interactioN

	def name(self, instance):
		return instance.info.first_name	


class open_courseS(resources.ModelResource):
	class Meta:
		model = open_courses


@admin.register(open_courses)
class Open_courses(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = open_courseS

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


class exclusive_researcH(resources.ModelResource):
	class Meta:
		model = exclusive_research


@admin.register(exclusive_research)
class Exclusive_research(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = exclusive_researcH

	def name(self, instance):
		return instance.info.first_name	

class conference_journaL(resources.ModelResource):
	class Meta:
		model = conference_journal


@admin.register(conference_journal)
class Conference_journal(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = conference_journaL

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



