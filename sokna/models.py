from django.db import models

from daira.models import Mol7aka
from daira.validators import PhoneValidator, TermsOfUse


class SoknaRequest(models.Model):

	class GENDER(models.IntegerChoices):
		MALE = (1, 'Male')
		FEMALE = (2, 'Female')


	class STATUS(models.IntegerChoices):
		PENDING = (0, 'Pending')
		APPROVED = (1, 'Approved')
		REJECTED = (2, 'Rejected')

	CIN 		= models.CharField(max_length=10)
	firstname 	= models.CharField(max_length=32)
	lastname 	= models.CharField(max_length=32)
	born 		= models.DateField(null=True, blank=True)
	gender 		= models.IntegerField(choices=GENDER.choices)
	photo_1 	= models.ImageField(upload_to='cin_photos')
	photo_2 	= models.ImageField(upload_to='cin_photos')
	phone 		= models.IntegerField(validators=[PhoneValidator])
	address 	= models.CharField(max_length=256)
	mol7aka 	= models.ForeignKey(Mol7aka, on_delete=models.DO_NOTHING, null=True)
	status 		= models.IntegerField(choices=STATUS.choices, default=STATUS.PENDING)
	terms_of_use = models.BooleanField(validators=[TermsOfUse], verbose_name='I confess that all the above information are correct.')

	class Meta:
		db_table = 'sokna_requests'

	def __str__(self):
		return f'{self.firstname} {self.lastname} ({self.CIN})'
