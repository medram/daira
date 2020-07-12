from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from classifier.models import Profile
from crispy_forms.helper import FormHelper


class UserRegistrationFrom(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(label='E-mail', disabled=True)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.use_custom_control = True
		self.helper.form_tag = False


class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('profile_image', 'phone', 'address')
		widgets = {
			'profile_image': forms.FileInput()
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.use_custom_control = True
		self.helper.form_tag = False