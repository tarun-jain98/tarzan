from django.db import models
from django.contrib.auth.models import AbstractUser, User

#TABLE-1

class Designation(models.Model):
	"""
	Description: Holds the Designations avbailable
	"""
	name = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name

class Field(models.Model):
	"""
	Description: Holds the Designations avbailable
	"""
	name = models.CharField(max_length=30, blank=True, null=True)

	def __str__(self):
		return self.name

class Year(models.Model):
	"""
	Description: Holds the Designations avbailable
	"""
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.year



class Department(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name

class author_type(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name

class agency_type(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name

class consultancy_type(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name

class status(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name

class investigator_type(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name


class index_type(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name

class int_ext(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name

class support(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name

class skills(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name


class User(AbstractUser):
	phone = models.BigIntegerField(null=True)
	department = models.ForeignKey('Department', on_delete=models.CASCADE,null=True)
	designation = models.ForeignKey('Designation', on_delete=models.CASCADE,null=True)
	teach_status = models.BooleanField(default=False)
	info = models.CharField(max_length=20, blank=True, null=True)


	def __str__(self):
		return self.username

	def is_assistant_professor(self):
		faculty = Designation.objects.get(pk=11)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_associate_professor(self):
		faculty = Designation.objects.get(pk=9)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_professor(self):
		faculty = Designation.objects.get(pk=10)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_hod(self):
		faculty = Designation.objects.get(pk=8)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_principal(self):
		faculty = Designation.objects.get(pk=7)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_ao(self):
		faculty = Designation.objects.get(pk=6)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def get_designation(self):
		return self.designation.name




class fdp(models.Model):

	type_fdp = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='type_fdp')
	name = models.CharField(max_length=50, blank=True, null=True)
	supported_by = models.ForeignKey('support', on_delete=models.CASCADE,null=True,related_name='supported_by')
	date_from = models.DateField(blank=True, null=True)
	date_to = models.DateField(blank=True, null=True)
	venue = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name

class refreshers_course(models.Model):
	# refreshers_course_id = models.AutoField(primary_key=True)
	type_refreshers_course = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='type_refreshers_course')
	name = models.CharField(max_length=50, blank=True, null=True)
	supported_by = models.ForeignKey('support', on_delete=models.CASCADE,null=True,related_name='supported_by1')
	date_from = models.DateField(blank=True, null=True)
	date_to = models.DateField(blank=True, null=True)
	venue = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name

class sttp(models.Model):
	# sttp_id = models.AutoField(primary_key=True)
	type_sttp = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='type_sttp')
	name = models.CharField(max_length=50, blank=True, null=True)
	supported_by = models.ForeignKey('support', on_delete=models.CASCADE,null=True,related_name='supported_by2')
	date_from = models.DateField(blank=True, null=True)
	date_to = models.DateField(blank=True, null=True)
	venue = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name

class workshop(models.Model):
	type_workshop = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='type_workshop')
	name = models.CharField(max_length=50, blank=True, null=True)
	supported_by = models.ForeignKey('support', on_delete=models.CASCADE,null=True,related_name='supported_by3')
	date_from = models.DateField(blank=True, null=True)
	date_to = models.DateField(blank=True, null=True)
	venue = models.CharField(max_length=50, blank=True, null=True)
	skills_acquired = models.ForeignKey('skills', on_delete=models.CASCADE,null=True,related_name='skills_acquired')
	skills_info = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name


class seminar(models.Model):
	# interaction_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50, blank=True, null=True)
	topic = models.CharField(max_length=50, blank=True, null=True)
	venue = models.CharField(max_length=50, blank=True, null=True)
	no_atttended = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name

class technical_talk(models.Model):
	# interaction_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50, blank=True, null=True)
	topic = models.CharField(max_length=50, blank=True, null=True)
	venue = models.CharField(max_length=50, blank=True, null=True)
	no_atttended = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name


class session_chair(models.Model):
	# interaction_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50, blank=True, null=True)
	topic = models.CharField(max_length=50, blank=True, null=True)
	venue = models.CharField(max_length=50, blank=True, null=True)
	no_atttended = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name



class online_courses(models.Model):
	# online_courses_id = models.AutoField(primary_key=True)
	name_course = models.CharField(max_length=50, blank=True, null=True)
	name_organization = models.CharField(max_length=50, blank=True, null=True)
	date_completed = models.DateField(blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)
	grade = models.CharField(max_length=10, blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name

class honours(models.Model):
	# honours_id = models.AutoField(primary_key=True)
	state_name_award = models.CharField(max_length=50, blank=True, null=True)
	state_name_organization = models.CharField(max_length=50, blank=True, null=True)
	state_area_acheivement = models.CharField(max_length=50, blank=True, null=True)
	state_brief_remarks = models.TextField( blank=True, null=True)

	national_name_award = models.CharField(max_length=50, blank=True, null=True)
	national_name_organization = models.CharField(max_length=50, blank=True, null=True)
	national_area_acheivement = models.CharField(max_length=50, blank=True, null=True)
	national_brief_remarks = models.TextField( blank=True, null=True)

	international_name_award = models.CharField(max_length=50, blank=True, null=True)
	international_name_organization = models.CharField(max_length=50, blank=True, null=True)
	international_area_acheivement = models.TextField( blank=True, null=True)
	international_brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)

	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name


class consultancy(models.Model):
	# consultancy_id = models.AutoField(primary_key=True)
	name_organization = models.CharField(max_length=50, blank=True, null=True)
	title = models.CharField(max_length=50, blank=True, null=True)
	consultancy_type = models.ForeignKey('consultancy_type', on_delete=models.CASCADE,null=True)
	date_approval = models.DateField(blank=True, null=True)
	value = models.CharField(max_length=10, blank=True, null=True)
	consultancy_status = models.ForeignKey('status', on_delete=models.CASCADE,null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name

class funding(models.Model):
	# funding_id = models.AutoField(primary_key=True)

	title_1 = models.CharField(max_length=50, blank=True, null=True)
	name_agency_1 = models.CharField(max_length=50, blank=True, null=True)
	agency_type_1 = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='agency_type_1')
	date_sanction_1 = models.DateField(blank=True, null=True)
	amount_sanction_1 = models.CharField(max_length=10, blank=True, null=True)
	from_date_1 = models.DateField(blank=True, null=True)
	to_date_1 = models.DateField(blank=True, null=True)
	place_1 = models.CharField(max_length=50, blank=True, null=True)
	investigator_type_1 = models.ForeignKey('investigator_type', on_delete=models.CASCADE,null=True,related_name='investigator_type_1')
	brief_remarks_1 = models.TextField( blank=True, null=True)

	title_2 = models.CharField(max_length=50, blank=True, null=True)
	name_agency_2 = models.CharField(max_length=50, blank=True, null=True)
	agency_type_2 = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='agency_type_2')
	date_sanction_2 = models.DateField(blank=True, null=True)
	amount_sanction_2 = models.CharField(max_length=10, blank=True, null=True)
	from_date_2 = models.DateField(blank=True, null=True)
	to_date_2 = models.DateField(blank=True, null=True)
	place_2 = models.CharField(max_length=50, blank=True, null=True)
	investigator_type_2 = models.ForeignKey('investigator_type', on_delete=models.CASCADE,null=True,related_name='investigator_type_2')
	brief_remarks_2 = models.TextField( blank=True, null=True)

	title_3 = models.CharField(max_length=50, blank=True, null=True)
	name_agency_3 = models.CharField(max_length=50, blank=True, null=True)
	agency_type_3 = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='agency_type_3')
	date_sanction_3 = models.DateField(blank=True, null=True)
	amount_sanction_3 = models.CharField(max_length=10, blank=True, null=True)
	from_date_3 = models.DateField(blank=True, null=True)
	to_date_3 = models.DateField(blank=True, null=True)
	place_3 = models.CharField(max_length=50, blank=True, null=True)
	investigator_type_3 = models.ForeignKey('investigator_type', on_delete=models.CASCADE,null=True,related_name='investigator_type_3')
	brief_remarks_3 = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name

# class exclusive_research(models.Model):
# 	# exclusive_research_id = models.AutoField(primary_key=True)
# 	name_organization_1 = models.CharField(max_length=50, blank=True, null=True)
# 	from_date_1 = models.DateField(blank=True, null=True)
# 	to_date_1 = models.DateField(blank=True, null=True)

# 	name_organization_2 = models.CharField(max_length=50, blank=True, null=True)
# 	from_date_2 = models.DateField(blank=True, null=True)
# 	to_date_2 = models.DateField(blank=True, null=True)

# 	name_organization_3 = models.CharField(max_length=50, blank=True, null=True)
# 	from_date_3 = models.DateField(blank=True, null=True)
# 	to_date_3 = models.DateField(blank=True, null=True)

# 	total_exp = models.CharField(max_length=10, blank=True, null=True)
# 	brief_remarks = models.TextField( blank=True, null=True)

# 	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
# 	year = models.CharField(max_length=20, blank=True, null=True)

# 	def __str__(self):
# 		return self.info.first_name

class conference(models.Model):
	# conference_journal_id = models.AutoField(primary_key=True)

	c1_name = models.CharField(max_length=500, blank=True, null=True)
	c1_title = models.CharField(max_length=500, blank=True, null=True)
	c1_place = models.CharField(max_length=500, blank=True, null=True)
	c1_date = models.DateField(blank=True, null=True)
	c1_author_type = models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='c1_author_type')
	c1_index_type = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='c1_index_type')
	c1_doi = models.CharField(max_length=500,blank=True, null=True)
	c1_url = models.CharField(max_length=500,blank=True, null=True)
	c1_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='c1_type')
	c1_issn = models.CharField(max_length=50,blank=True, null=True)
	c1_isbn = models.CharField(max_length=50,blank=True, null=True)

	c2_name = models.CharField(max_length=500, blank=True, null=True)
	c2_title = models.CharField(max_length=500, blank=True, null=True)
	c2_place = models.CharField(max_length=500, blank=True, null=True)
	c2_date = models.DateField(blank=True, null=True)
	c2_author_type = models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='c2_author_type')
	c2_index_type = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='c2_index_type')
	c2_doi = models.CharField(max_length=500,blank=True, null=True)
	c2_url = models.CharField(max_length=500,blank=True, null=True)
	c2_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='c2_type')
	c2_issn = models.CharField(max_length=50,blank=True, null=True)
	c2_isbn = models.CharField(max_length=50,blank=True, null=True)

	c3_name = models.CharField(max_length=500, blank=True, null=True)
	c3_title = models.CharField(max_length=500, blank=True, null=True)
	c3_place = models.CharField(max_length=500, blank=True, null=True)
	c3_date = models.DateField(blank=True, null=True)
	c3_author_type = models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='c3_author_type')
	c3_index_type = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='c3_index_type')
	c3_doi = models.CharField(max_length=500,blank=True, null=True)
	c3_url = models.CharField(max_length=500,blank=True, null=True)
	c3_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='c3_type')
	c3_issn = models.CharField(max_length=50,blank=True, null=True)
	c3_isbn = models.CharField(max_length=50,blank=True, null=True)

	c4_name = models.CharField(max_length=500, blank=True, null=True)
	c4_title = models.CharField(max_length=500, blank=True, null=True)
	c4_place = models.CharField(max_length=500, blank=True, null=True)
	c4_date = models.DateField(blank=True, null=True)
	c4_author_type = models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='c4_author_type')
	c4_index_type = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='c4_index_type')
	c4_doi = models.CharField(max_length=500,blank=True, null=True)
	c4_url = models.CharField(max_length=500,blank=True, null=True)
	c4_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='c4_type')
	c4_issn = models.CharField(max_length=50,blank=True, null=True)
	c4_isbn = models.CharField(max_length=50,blank=True, null=True)

	c5_name = models.CharField(max_length=500, blank=True, null=True)
	c5_title = models.CharField(max_length=500, blank=True, null=True)
	c5_place = models.CharField(max_length=500, blank=True, null=True)
	c5_date = models.DateField(blank=True, null=True)
	c5_author_type = models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='c5_author_type')
	c5_index_type = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='c5_index_type')
	c5_doi = models.CharField(max_length=500,blank=True, null=True)
	c5_url = models.CharField(max_length=500,blank=True, null=True)
	c5_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='c5_type')
	c5_issn = models.CharField(max_length=50,blank=True, null=True)
	c5_isbn = models.CharField(max_length=50,blank=True, null=True)

	c6_name = models.CharField(max_length=500, blank=True, null=True)
	c6_title = models.CharField(max_length=500, blank=True, null=True)
	c6_place = models.CharField(max_length=500, blank=True, null=True)
	c6_date = models.DateField(blank=True, null=True)
	c6_author_type = models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='c6_author_type')
	c6_index_type = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='c6_index_type')
	c6_doi = models.CharField(max_length=500,blank=True, null=True)
	c6_url = models.CharField(max_length=500,blank=True, null=True)
	c6_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='c6_type')
	c6_issn = models.CharField(max_length=50,blank=True, null=True)
	c6_isbn = models.CharField(max_length=50,blank=True, null=True)

	c7_name = models.CharField(max_length=500, blank=True, null=True)
	c7_title = models.CharField(max_length=500, blank=True, null=True)
	c7_place = models.CharField(max_length=500, blank=True, null=True)
	c7_date = models.DateField(blank=True, null=True)
	c7_author_type = models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='c7_author_type')
	c7_index_type = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='c7_index_type')
	c7_doi = models.CharField(max_length=500,blank=True, null=True)
	c7_url = models.CharField(max_length=500,blank=True, null=True)
	c7_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='c7_type')
	c7_issn = models.CharField(max_length=50,blank=True, null=True)
	c7_isbn = models.CharField(max_length=50,blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name



class journal(models.Model):
	j1_index = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='j_index')
	j1_name = models.CharField(max_length=500, blank=True, null=True)
	j1_title = models.CharField(max_length=500, blank=True, null=True)
	j1_volume = models.CharField(max_length=500, blank=True, null=True)
	j1_issn = models.CharField(max_length=500, blank=True, null=True)
	j1_date = models.DateField(blank=True, null=True)
	j1_page = models.CharField(max_length=500,blank=True, null=True)
	j1_author =	models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='j1_author_type')
	j1_doi = models.CharField(max_length=500,blank=True, null=True)
	j1_url = models.CharField(max_length=500,blank=True, null=True)
	j1_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='j1_type')
	j1_isbn = models.CharField(max_length=50,blank=True, null=True)


	j2_index = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='j2_index')
	j2_name = models.CharField(max_length=500, blank=True, null=True)
	j2_title = models.CharField(max_length=500, blank=True, null=True)
	j2_volume = models.CharField(max_length=500, blank=True, null=True)
	j2_issn = models.CharField(max_length=500, blank=True, null=True)
	j2_date = models.DateField(blank=True, null=True)
	j2_page = models.CharField(max_length=500,blank=True, null=True)
	j2_author =	models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='j2_author_type')
	j2_doi = models.CharField(max_length=500,blank=True, null=True)
	j2_url = models.CharField(max_length=500,blank=True, null=True)
	j2_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='j2_type')
	j2_isbn = models.CharField(max_length=50,blank=True, null=True)


	j3_index = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='j3_index')
	j3_name = models.CharField(max_length=500, blank=True, null=True)
	j3_title = models.CharField(max_length=500, blank=True, null=True)
	j3_volume = models.CharField(max_length=500, blank=True, null=True)
	j3_issn = models.CharField(max_length=500, blank=True, null=True)
	j3_date = models.DateField(blank=True, null=True)
	j3_page = models.CharField(max_length=500,blank=True, null=True)
	j3_author =	models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='j3_author_type')
	j3_doi = models.CharField(max_length=500,blank=True, null=True)
	j3_url = models.CharField(max_length=500,blank=True, null=True)
	j3_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='j3_type')
	j3_isbn = models.CharField(max_length=50,blank=True, null=True)

	j4_index = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='j4_index')
	j4_name = models.CharField(max_length=500, blank=True, null=True)
	j4_title = models.CharField(max_length=500, blank=True, null=True)
	j4_volume = models.CharField(max_length=500, blank=True, null=True)
	j4_issn = models.CharField(max_length=500, blank=True, null=True)
	j4_date = models.DateField(blank=True, null=True)
	j4_page = models.CharField(max_length=500,blank=True, null=True)
	j4_author =	models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='j4_author_type')
	j4_doi = models.CharField(max_length=500,blank=True, null=True)
	j4_url = models.CharField(max_length=500,blank=True, null=True)
	j4_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='j4_type')
	j4_isbn = models.CharField(max_length=50,blank=True, null=True)

	j5_index = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='j5_index')
	j5_name = models.CharField(max_length=500, blank=True, null=True)
	j5_title = models.CharField(max_length=500, blank=True, null=True)
	j5_volume = models.CharField(max_length=500, blank=True, null=True)
	j5_issn = models.CharField(max_length=500, blank=True, null=True)
	j5_date = models.DateField(blank=True, null=True)
	j5_page = models.CharField(max_length=500,blank=True, null=True)
	j5_author =	models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='j5_author_type')
	j5_doi = models.CharField(max_length=500,blank=True, null=True)
	j5_url = models.CharField(max_length=500,blank=True, null=True)
	j5_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='j5_type')
	j5_isbn = models.CharField(max_length=50,blank=True, null=True)


	j6_index = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='j6_index')
	j6_name = models.CharField(max_length=500, blank=True, null=True)
	j6_title = models.CharField(max_length=500, blank=True, null=True)
	j6_volume = models.CharField(max_length=500, blank=True, null=True)
	j6_issn = models.CharField(max_length=500, blank=True, null=True)
	j6_date = models.DateField(blank=True, null=True)
	j6_page = models.CharField(max_length=500,blank=True, null=True)
	j6_author =	models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='j6_author_type')
	j6_doi = models.CharField(max_length=500,blank=True, null=True)
	j6_url = models.CharField(max_length=500,blank=True, null=True)
	j6_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='j6_type')
	j6_isbn = models.CharField(max_length=50,blank=True, null=True)

	j7_index = models.ForeignKey('index_type', on_delete=models.CASCADE,null=True,related_name='j7_index')
	j7_name = models.CharField(max_length=500, blank=True, null=True)
	j7_title = models.CharField(max_length=500, blank=True, null=True)
	j7_volume = models.CharField(max_length=500, blank=True, null=True)
	j7_issn = models.CharField(max_length=500, blank=True, null=True)
	j7_date = models.DateField(blank=True, null=True)
	j7_page = models.CharField(max_length=500,blank=True, null=True)
	j7_author =	models.ForeignKey('author_type', on_delete=models.CASCADE,null=True,related_name='j7_author_type')
	j7_doi = models.CharField(max_length=500,blank=True, null=True)
	j7_url = models.CharField(max_length=500,blank=True, null=True)
	j7_type = models.ForeignKey('agency_type', on_delete=models.CASCADE,null=True,related_name='j7_type')
	j7_isbn = models.CharField(max_length=50,blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name



class book(models.Model):
	# book_id = models.AutoField(primary_key=True)
	number = models.CharField(max_length=50, blank=True, null=True)
	title = models.CharField(max_length=50, blank=True, null=True)
	author =	models.ForeignKey('author_type', on_delete=models.CASCADE,null=True)
	edition = models.CharField(max_length=50, blank=True, null=True)
	volume = models.CharField(max_length=50, blank=True, null=True)
	publisher = models.CharField(max_length=50, blank=True, null=True)
	isbn = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name


class chapter(models.Model):
	# book_id = models.AutoField(primary_key=True)
	number = models.CharField(max_length=50, blank=True, null=True)
	title = models.CharField(max_length=50, blank=True, null=True)
	author = models.ForeignKey('author_type', on_delete=models.CASCADE,null=True)
	name_book = models.CharField(max_length=50, blank=True, null=True)
	chapter_no = models.CharField(max_length=50, blank=True, null=True)
	page_no = models.CharField(max_length=50, blank=True, null=True)
	publisher = models.CharField(max_length=50, blank=True, null=True)
	brief_remarks = models.TextField( blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name


class phd_guide(models.Model):
	# phd_guide_id = models.AutoField(primary_key=True)

	name_student_1 = models.CharField(max_length=50, blank=True, null=True)
	int_ext_1 = models.ForeignKey('int_ext', on_delete=models.CASCADE,null=True,related_name='int_ext_1')
	name_university_1 = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre_1 = models.CharField(max_length=50, blank=True, null=True)
	year_1 = models.CharField(max_length=50, blank=True, null=True)
	area_1 = models.CharField(max_length=50, blank=True, null=True)
	phd_status_1 = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='phd_status_1')
	co_guide_1 = models.CharField(max_length=50, blank=True, null=True)

	name_student_2 = models.CharField(max_length=50, blank=True, null=True)
	int_ext_2 = models.ForeignKey('int_ext', on_delete=models.CASCADE,null=True,related_name='int_ext_2')
	name_university_2 = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre_2 = models.CharField(max_length=50, blank=True, null=True)
	year_2 = models.CharField(max_length=50, blank=True, null=True)
	area_2 = models.CharField(max_length=50, blank=True, null=True)
	phd_status_2 = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='phd_status_2')
	co_guide_2 = models.CharField(max_length=50, blank=True, null=True)


	name_student_3 = models.CharField(max_length=50, blank=True, null=True)
	int_ext_3 = models.ForeignKey('int_ext', on_delete=models.CASCADE,null=True,related_name='int_ext_3')
	name_university_3 = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre_3 = models.CharField(max_length=50, blank=True, null=True)
	year_3 = models.CharField(max_length=50, blank=True, null=True)
	area_3 = models.CharField(max_length=50, blank=True, null=True)
	phd_status_3 = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='phd_status_3')
	co_guide_3 = models.CharField(max_length=50, blank=True, null=True)

	name_student_4 = models.CharField(max_length=50, blank=True, null=True)
	int_ext_4 = models.ForeignKey('int_ext', on_delete=models.CASCADE,null=True,related_name='int_ext_4')
	name_university_4 = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre_4 = models.CharField(max_length=50, blank=True, null=True)
	year_4 = models.CharField(max_length=50, blank=True, null=True)
	area_4 = models.CharField(max_length=50, blank=True, null=True)
	phd_status_4 = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='phd_status_4')
	co_guide_4 = models.CharField(max_length=50, blank=True, null=True)

	name_student_5 = models.CharField(max_length=50, blank=True, null=True)
	int_ext_5 = models.ForeignKey('int_ext', on_delete=models.CASCADE,null=True,related_name='int_ext_5')
	name_university_5 = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre_5 = models.CharField(max_length=50, blank=True, null=True)
	year_5 = models.CharField(max_length=50, blank=True, null=True)
	area_5 = models.CharField(max_length=50, blank=True, null=True)
	phd_status_5 = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='phd_status_5')
	co_guide_5 = models.CharField(max_length=50, blank=True, null=True)

	name_student_6 = models.CharField(max_length=50, blank=True, null=True)
	int_ext_6 = models.ForeignKey('int_ext', on_delete=models.CASCADE,null=True,related_name='int_ext_6')
	name_university_6 = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre_6 = models.CharField(max_length=50, blank=True, null=True)
	year_6 = models.CharField(max_length=50, blank=True, null=True)
	area_6 = models.CharField(max_length=50, blank=True, null=True)
	phd_status_6 = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='phd_status_6')
	co_guide_6 = models.CharField(max_length=50, blank=True, null=True)


	name_student_7 = models.CharField(max_length=50, blank=True, null=True)
	int_ext_7 = models.ForeignKey('int_ext', on_delete=models.CASCADE,null=True,related_name='int_ext_7')
	name_university_7 = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre_7 = models.CharField(max_length=50, blank=True, null=True)
	year_7 = models.CharField(max_length=50, blank=True, null=True)
	area_7 = models.CharField(max_length=50, blank=True, null=True)
	phd_status_7 = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='phd_status_7')
	co_guide_7 = models.CharField(max_length=50, blank=True, null=True)

	name_student_8 = models.CharField(max_length=50, blank=True, null=True)
	int_ext_8 = models.ForeignKey('int_ext', on_delete=models.CASCADE,null=True,related_name='int_ext_8')
	name_university_8 = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre_8 = models.CharField(max_length=50, blank=True, null=True)
	year_8 = models.CharField(max_length=50, blank=True, null=True)
	area_8 = models.CharField(max_length=50, blank=True, null=True)
	phd_status_8 = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='phd_status_8')
	co_guide_8 = models.CharField(max_length=50, blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name

class phd_self(models.Model):
	# phd_self_id = models.AutoField(primary_key=True)
	name_guide = models.CharField(max_length=50, blank=True, null=True)
	name_co_guide = models.CharField(max_length=50, blank=True, null=True)
	name_university = models.CharField(max_length=50, blank=True, null=True)
	name_research_centre = models.CharField(max_length=50, blank=True, null=True)
	area = models.CharField(max_length=50, blank=True, null=True)
	year = models.CharField(max_length=50, blank=True, null=True)
	phd_status = models.ForeignKey('status', on_delete=models.CASCADE,null=True,related_name='status')


	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	year = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.info.first_name
