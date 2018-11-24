from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

admin.site.site_header = "Tarzan System";

admin.site.register(Designation)

admin.site.register(Department)

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



