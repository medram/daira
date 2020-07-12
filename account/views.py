from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.http import is_safe_url
from django.conf import settings

from classifier.models import Profile

from . import forms
from .decorators import anonymous_required, user_status_required


@login_required
@user_status_required(Profile.Status.APPROVED)
def index(req):
	return render(req, 'account/index.html')


@login_required
@user_status_required(Profile.Status.APPROVED)
def profile(req):

	if req.method == 'POST':
		user_form = forms.UserUpdateForm(req.POST, instance=req.user)
		profile_form = forms.ProfileUpdateForm(req.POST, req.FILES, instance=req.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(req, 'Saved Successfully.')
			return redirect('account:profile')
	else:
		user_form = forms.UserUpdateForm(instance=req.user)
		profile_form = forms.ProfileUpdateForm(instance=req.user.profile)

	options = {
		'user_form': user_form,
		'profile_form': profile_form
	}
	return render(req, 'account/profile.html', options)


@anonymous_required
def login(req):
	if req.method == 'POST':
		username = req.POST.get('username')
		password = req.POST.get('password')

		if username == '' or password == '':
			messages.warning(req, 'Please insert your credentials to login.')
			return redirect('account:login')
		else:
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				# check if the user is approved to logged him in.
				if user.profile.status == Profile.Status.APPROVED:
					# Login this valid user.
					auth.login(req, user)

					# redirect to the next page.
					next_url = req.GET.get('next')
					is_safe = is_safe_url(url=next_url, allowed_hosts=settings.ALLOWED_HOSTS, require_https=req.is_secure())
					
					if next_url and is_safe and 'logout' not in next_url:
						return redirect(next_url)
					return redirect('account:index')

				elif user.profile.status == Profile.Status.BANNED:
					messages.error(req, 'Oops! Your account has been banned.')
			else:
				messages.warning(req, 'Oops! Invalid credentials, Please try again.')
			return redirect('account:login')

	options = {
		'page': {
			'title': 'Login to my Account'
		}
	}
	return render(req, 'account/login.html', options)


@anonymous_required
def register(req):
	if req.method == 'POST':
		form = forms.UserRegistrationFrom(req.POST)

		if form.is_valid():
			form.save()
			messages.success(req, 'Registered successfully, You could login now.')
			return redirect('account:login')
	else:
		form = forms.UserRegistrationFrom()


	options = {
		'page': {
			'title': 'Register a new account'
		},
		'form': form
	}
	return render(req, 'account/register.html', options)


@login_required
def logout(req):
	auth.logout(req)
	messages.success(req, 'You are now logged out.')
	return redirect('account:login')


# @anonymous_required
# def password_reset(req):
# 	form = forms.PasswordResetForm()
# 	if req.method == 'POST':
# 		form = forms.PasswordResetForm(req.POST)
# 		if form.is_valid():
# 			form.save(domain_override='localhost')
# 			messages.success(req, 'An Email has been sent to reset your password.')
# 			return redirect('account:password_reset')

# 	options = {
# 		'form': form,
# 		'page': {
# 			'title': 'Reset Password'
# 		}
# 	}
# 	return render(req, 'account/password_reset.html', options)
