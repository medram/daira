from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _, get_language

class Individual(models.Model):

	MALE = 1
	FEMALE = 2

	GENDER = [
		(MALE, _('Male')),
		(FEMALE, _('Female'))
	]

	CIN 		= models.CharField(max_length=10, primary_key=True)
	firstname 	= models.CharField(max_length=32)
	lastname 	= models.CharField(max_length=32)
	born 		= models.DateField(null=True, blank=True)
	gender 		= models.IntegerField(choices=GENDER, default=MALE)
	jobs		= models.ManyToManyField('Job', related_name='individuals') 
	handicapped = models.BooleanField(default=False)

	relation 	= models.ManyToManyField('self', through='Relationship', through_fields=('individual_1', 'individual_2'))
	mol7aka 	= models.ForeignKey('Mol7aka', on_delete=models.CASCADE, related_name='individuals', null=True, blank=True)

	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'individuals'

	def __str__(self):
		return f'{self.firstname} {self.lastname} ({self.CIN})'


class Job(models.Model):
	job_name = models.CharField(max_length=64)

	class Meta:
		db_table = 'jobs'

	def __str__(self):
		return self.job_name


class Relationship(models.Model):
	individual_1 	= models.ForeignKey('Individual', on_delete=models.CASCADE, related_name='individual_1')
	individual_2 	= models.ForeignKey('Individual', on_delete=models.CASCADE, related_name='individual_2')
	relationship_type = models.ForeignKey('RelationshipType', on_delete=models.DO_NOTHING, null=True)
	description 	= RichTextField(null=True) 

	mol7aka 	= models.ForeignKey('Mol7aka', on_delete=models.CASCADE, related_name='relationships', null=True, blank=True)

	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)


class RelationshipType(models.Model):
	relationship_name = models.CharField(max_length=64)

	def __str__(self):
		return self.relationship_name



class Address(models.Model):
	address 	= models.CharField(max_length=256)
	street 		= models.ForeignKey('Street', on_delete=models.DO_NOTHING, null=True, related_name='addresses')
	city 		= models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
	zip_code 	= models.CharField(max_length=16, null=True, blank=True)
	individual  = models.ForeignKey('Individual', on_delete=models.SET_NULL, null=True, blank=True)

	mol7aka 	= models.ForeignKey('Mol7aka', on_delete=models.CASCADE, related_name='addresses', null=True, blank=True)

	class Meta:
		db_table = 'addresses'
		verbose_name_plural = 'addresses'


	def __str__(self):
		return f'{self.address}'


class City(models.Model):
	city = models.CharField(max_length=32)

	class Meta:
		db_table = 'cities'
		verbose_name = 'city'
		verbose_name_plural = 'cities'

	def __str__(self):
		return self.city

class Street(models.Model):
	street_name = models.CharField(max_length=64)
	mol7aka 	= models.ForeignKey('Mol7aka', on_delete=models.CASCADE, related_name='streets', null=True, blank=True)

	class Meta:
		db_table = 'streets'

	def __str__(self):
		return self.street_name


class Report(models.Model):
	report = RichTextField()
	individual = models.ForeignKey('individual', on_delete=models.CASCADE, related_name='reports')
	mol7aka 	= models.ForeignKey('Mol7aka', on_delete=models.CASCADE, related_name='reports', null=True, blank=True)

	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'report ({self.pk}) - {self.individual}'


class Amala(models.Model):
	name = models.CharField(max_length=32)
	name_in_arabic = models.CharField(max_length=32)

	class Meta:
		verbose_name = _('Amala')
		verbose_name_plural = _('Amalat')

	def __str__(self):
		if get_language() == 'ar':
			return self.name_in_arabic
		return self.name

class Mol7aka(models.Model):
	name = models.CharField(max_length=32)
	name_in_arabic = models.CharField(max_length=32)
	
	amala = models.ForeignKey('Amala', on_delete=models.CASCADE, related_name='mol7akat')

	class Meta:
		verbose_name = _('Administrative attache')
		verbose_name_plural = _('Administrative attaches')

	def __str__(self):
		if get_language() == 'ar':
			return self.name_in_arabic
		return self.name
