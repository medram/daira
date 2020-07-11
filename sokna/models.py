from django.db import models
from django.utils.translation import gettext_lazy as _

from daira.models import Mol7aka
from daira.validators import PhoneValidator, TermsOfUse

class SoknaRequest(models.Model):

	class GENDER(models.IntegerChoices):
		MALE = (1, _('Male'))
		FEMALE = (2, _('Female'))


	class STATUS(models.IntegerChoices):
		PENDING = (0, _('Pending'))
		APPROVED = (1, _('Approved'))
		REJECTED = (2, _('Rejected'))

	CIN 		= models.CharField(max_length=10, verbose_name=_('CIN'))
	firstname 	= models.CharField(max_length=32, verbose_name=_("Fistname"))
	lastname 	= models.CharField(max_length=32, verbose_name=_("Lastname"))
	
	born_d 		= models.IntegerField(null=True, blank=True, verbose_name=_('Day of birth'))
	born_m 		= models.IntegerField(null=True, blank=True, verbose_name=_('Month of birth'))
	born_y 		= models.IntegerField(null=True, blank=True, verbose_name=_('Year of birth'))
	born_no_d_m = models.BooleanField(default=False, null=True, blank=True, verbose_name=_('I don\'t have day & month of my birthday'))

	gender 		= models.IntegerField(choices=GENDER.choices, verbose_name=_('Gender'))
	photo_1 	= models.ImageField(upload_to='cin_photos', verbose_name=_('Front face of CIN'))
	photo_2 	= models.ImageField(upload_to='cin_photos', verbose_name=_('Back face of CIN'))
	phone 		= models.BigIntegerField(validators=[PhoneValidator], verbose_name=_('Phone number'))
	address 	= models.CharField(max_length=256, verbose_name=_('Current residence Address'))
	mol7aka 	= models.ForeignKey(Mol7aka, on_delete=models.DO_NOTHING, null=True, verbose_name=_('Administrative attache'))
	status 		= models.IntegerField(choices=STATUS.choices, default=STATUS.PENDING)
	terms_of_use = models.BooleanField(default=False, validators=[TermsOfUse], verbose_name=_('I confess that all the above information are correct.'))

	notes 		= models.TextField(null=True, blank=True, verbose_name=_('Notes'))

	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'sokna_requests'
		verbose_name = _('Residential statement order')
		verbose_name_plural = _('Residential statement orders')

	def __str__(self):
		return f'{self.firstname} {self.lastname} ({self.CIN})'
