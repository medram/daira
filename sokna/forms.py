from django import forms

from .models import SoknaRequest

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SoknaRequestForm(forms.ModelForm):
	
	born = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'dd/mm/yyyy', 'autocomplete': 'off'}), required=False)
	photo_1 = forms.ImageField(widget=forms.FileInput(), label='Front face of CIN')
	photo_2 = forms.ImageField(widget=forms.FileInput(), label='Back face of CIN')

	class Meta:
		model = SoknaRequest
		fields = ('firstname', 'lastname', 'CIN', 'born', 'gender', 'phone', 'address', 'mol7aka',
			'photo_1', 'photo_2', 'terms_of_use')
		widgets = {
			'photo_1': forms.FileInput(),
			'photo_2': forms.FileInput()
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		# self.helper.form_method = 'post'
		# self.helper.use_custom_control = True
		# self.helper.form_tag = False
		# self.helper.add_input(Submit('submit', 'Submit'))

