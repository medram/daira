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
	firstname 	= models.CharField(max_length=32, verbose_name='الإسم')
	lastname 	= models.CharField(max_length=32, verbose_name='النسب')
	
	born_d 		= models.IntegerField(null=True, blank=True, verbose_name='يوم الإزدياد')
	born_m 		= models.IntegerField(null=True, blank=True, verbose_name='شهر الإزدياد')
	born_y 		= models.IntegerField(null=True, blank=True, verbose_name='سنة الإزدياد')
	born_no_d_m = models.BooleanField(default=False, null=True, blank=True, verbose_name='لا أتوفر على يوم و شهر الإزدياد')

	gender 		= models.IntegerField(choices=GENDER.choices, verbose_name='الجنس')
	photo_1 	= models.ImageField(upload_to='cin_photos', verbose_name='الجهة الأمامية  لبطاقة التعريف الوطنية')
	photo_2 	= models.ImageField(upload_to='cin_photos', verbose_name='الجهة الخلفية لبطاقة التعريف الوطنية')
	phone 		= models.BigIntegerField(validators=[PhoneValidator], verbose_name='رقم الهاتف')
	address 	= models.CharField(max_length=256, verbose_name='العنوان المقيم به حاليا')
	mol7aka 	= models.ForeignKey(Mol7aka, on_delete=models.DO_NOTHING, null=True, verbose_name='الملحقة الادارية')
	status 		= models.IntegerField(choices=STATUS.choices, default=STATUS.PENDING)
	terms_of_use = models.BooleanField(default=False, validators=[TermsOfUse], verbose_name='أصرح بصحة المعلومات المدخلة أعلاه.')

	notes 		= models.TextField(null=True, blank=True)

	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'sokna_requests'
		verbose_name = 'sokna submission'

	def __str__(self):
		return f'{self.firstname} {self.lastname} ({self.CIN})'


# class SoknaRequest(models.Model):

# 	class GENDER(models.IntegerChoices):
# 		MALE = (1, 'Male')
# 		FEMALE = (2, 'Female')


# 	class STATUS(models.IntegerChoices):
# 		PENDING = (0, 'Pending')
# 		APPROVED = (1, 'Approved')
# 		REJECTED = (2, 'Rejected')

# 	CIN 		= models.CharField(max_length=10)
# 	firstname 	= models.CharField(max_length=32)
# 	lastname 	= models.CharField(max_length=32)
	
# 	born_d 		= models.IntegerField(null=True, blank=True, verbose_name='Day of birthday')
# 	born_m 		= models.IntegerField(null=True, blank=True, verbose_name='Month of birthday')
# 	born_y 		= models.IntegerField(null=True, blank=True, verbose_name='Year of birthday')
# 	born_no_d_m = models.BooleanField(default=False, null=True, blank=True, verbose_name='I don\'t have day & month of my birthday')

# 	gender 		= models.IntegerField(choices=GENDER.choices)
# 	photo_1 	= models.ImageField(upload_to='cin_photos')
# 	photo_2 	= models.ImageField(upload_to='cin_photos')
# 	phone 		= models.BigIntegerField(validators=[PhoneValidator])
# 	address 	= models.CharField(max_length=256)
# 	mol7aka 	= models.ForeignKey(Mol7aka, on_delete=models.DO_NOTHING, null=True)
# 	status 		= models.IntegerField(choices=STATUS.choices, default=STATUS.PENDING)
# 	terms_of_use = models.BooleanField(default=False, validators=[TermsOfUse], verbose_name='I confess that all the above information are correct.')

# 	notes 		= models.TextField(null=True, blank=True)

# 	created 	= models.DateTimeField(auto_now_add=True)
# 	updated 	= models.DateTimeField(auto_now=True)

# 	class Meta:
# 		db_table = 'sokna_requests'
# 		verbose_name = 'sokna submission'

# 	def __str__(self):
# 		return f'{self.firstname} {self.lastname} ({self.CIN})'