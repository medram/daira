from django.db import models
from ckeditor.fields import RichTextField


class Individual(models.Model):

	UNKNOWN = 0
	MALE = 1
	FEMALE = 2

	GENDER = [
		(UNKNOWN, 'Unknown'),
		(MALE, 'Male'),
		(FEMALE, 'Female')
	]

	CIN 		= models.CharField(max_length=10, primary_key=True)
	firstname 	= models.CharField(max_length=32)
	lastname 	= models.CharField(max_length=32)
	born 		= models.DateField(null=True, blank=True)
	gender 		= models.IntegerField(choices=GENDER, default=UNKNOWN)
	jobs		= models.ManyToManyField('Job', related_name='individuals') 
	handicapped = models.BooleanField(default=False)

	relation 	= models.ManyToManyField('self', through='Relationship', through_fields=('individual_1', 'individual_2'))

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

	class Meta:
		db_table = 'addresses'
		verbose_name_plural = 'addresses'


	def __str__(self):
		return f'{self.address} {self.street}'


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

	class Meta:
		db_table = 'streets'

	def __str__(self):
		return self.street_name


class Report(models.Model):
	report = RichTextField()
	individual = models.ForeignKey('individual', on_delete=models.CASCADE, related_name='reports')

	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'report ({self.pk}) - {self.individual}'


class Amala(models.Model):
	name = models.CharField(max_length=32)

	class Meta:
		verbose_name_plural = 'Amalat'

	def __str__(self):
		return self.name


class Mol7aka(models.Model):
	name = models.CharField(max_length=32)
	amala = models.ForeignKey('Amala', on_delete=models.CASCADE, related_name='mol7akat')

	class Meta:
		verbose_name_plural = 'Mol7akat'

	def __str__(self):
		return self.name
