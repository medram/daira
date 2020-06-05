from django.shortcuts import render

from .forms import SoknaRequestForm

def register(req):

	form = SoknaRequestForm()

	page = {
		'title': 'sokna'
	}
	return render(req, 'sokna/register.html', {'page': page, 'form': form})
