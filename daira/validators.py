from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

def PhoneValidator(value):
	if type(value) is not int or not (len(value) == 10 and str(value).startswith('0')) \
		or not (len(value) == 12 and str(value).startswith('212')):
		raise ValidationError('This phone number is invalid.')


def TermsOfUse(value):
	if not value:
		raise ValidationError('Please accept terms of use.')