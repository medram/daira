from django import forms
from django.utils.translation import gettext_lazy as _

from .models import SoknaRequest

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SoknaRequestForm(forms.ModelForm):
	# born_d = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'dd', 'autocomplete': 'off', 'class': 'dateinput_d'}),
	# 							required=False, label='Day of birth')
	# born_m = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'mm', 'autocomplete': 'off', 'class': 'dateinput_m'}),
	# 							required=False, label='Month of birth')
	# born_y = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'yyyy', 'autocomplete': 'off', 'class': 'dateinput_y'}),
	# 							label='Year of birth')
	# born_no_d_m = forms.BooleanField(label='I don\'t have day & month of my birthday', required=False)

	# photo_1 = forms.ImageField(widget=forms.FileInput(), label='Front face of CIN')
	# photo_2 = forms.ImageField(widget=forms.FileInput(), label='Back face of CIN')

	born_d = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'dd', 'autocomplete': 'off', 'class': 'dateinput_d'}),
								required=False, label=_('Day of birth'))
	born_m = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'mm', 'autocomplete': 'off', 'class': 'dateinput_m'}),
								required=False, label=_('Month of birth'))
	born_y = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'yyyy', 'autocomplete': 'off', 'class': 'dateinput_y'}),
								label=_('Year of birth'))
	born_no_d_m = forms.BooleanField(label=_('I don\'t have day & month of my birthday'), required=False)

	photo_1 = forms.ImageField(widget=forms.FileInput(), label=_('Front face of CIN'))
	photo_2 = forms.ImageField(widget=forms.FileInput(), label=_('Back face of CIN'))

	class Meta:
		model = SoknaRequest
		fields = ('firstname', 'lastname', 'CIN', 'born_d', 'born_m', 'born_y', 'born_no_d_m', 'gender', 'phone', 'address', 'mol7aka',
			'photo_1', 'photo_2', 'terms_of_use')
		# widgets = {}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		# self.helper.form_method = 'post'
		# self.helper.use_custom_control = True
		# self.helper.form_tag = False
		# self.helper.add_input(Submit('submit', 'Submit'))


class FollowForm(forms.Form):
	CIN = forms.CharField(label=_('CIN'))
	submission_code = forms.CharField(label=_('Statement Code'))