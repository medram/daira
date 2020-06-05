from django.http import Http404 
from django.shortcuts import render
from .models import Page

# Create your views here.
def index(req, slug):
	try:
		page = Page.objects.filter(slug=slug.lower()).get(published=True)
		options = { 'page': page }
	except Page.DoesNotExist:
		raise Http404('Page Not Found!')
	return render(req, 'pages/page.html', options)


def error_404(req, exception):
	return render(req, 'pages/errors/404.html', status=404)

def error_403(req, exception):
	return render(req, 'pages/errors/403.html', status=403)

def error_500(req):
	return render(req, 'pages/errors/500.html', status=500)