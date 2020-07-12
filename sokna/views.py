from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import SoknaRequestForm, FollowForm
from .models import SoknaRequest

def register(req):

	if req.method == 'POST':
		form = SoknaRequestForm(req.POST, req.FILES)
		if form.is_valid():
			instance = form.save()
			messages.success(req, '<i class="fa fa-fw fa-check"></i> %s' % _('Your request has been submitted successfully.'))
			# redirect to a valid page.
			return redirect('sokna:done', id=instance.pk)
	else:
		form = SoknaRequestForm()


	page = {
		'title': 'sokna'
	}
	return render(req, 'sokna/register.html', {'page': page, 'form': form})


def done(req, id=None):

	return render(req, 'sokna/done.html', {'code': id})


def follow(req):
	SR = None
	if req.GET.get('CIN', None):
		form = FollowForm(req.GET)
		if form.is_valid():
			# TODO: get SoknaRequest and show its status & notes
			try:
				SR = SoknaRequest.objects.get(id=form.cleaned_data['submission_code'], CIN=form.cleaned_data['CIN'])
			except SoknaRequest.DoesNotExist:
				messages.warning(req, 'Oops! There is no submission')
				return redirect('sokna:follow')
	else:
		form = FollowForm()

	page = {
		'title': 'Follow submission'
	}

	return render(req, 'sokna/follow.html', {'page': page, 'form': form, 'sokna_request': SR})


def index(req):

	return render(req, 'sokna/index.html')