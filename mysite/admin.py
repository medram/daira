from django.contrib import admin
from django.utils import translation

# My custom AdminSite
class MyAdminSite(admin.AdminSite):

	def index(self, request, extra_context=None):
		if extra_context is None:
			extra_context = {}
		# Adding my context here
		extra_context.update({
			'servers': 0,
			'profiles': 0,
			'proxies': 0,
			'queues': 0,
			'tasks': 0,
			'workers': 0
		})
		return super().index(request, extra_context=extra_context)