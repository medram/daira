from django.contrib import admin
from django.utils import translation
from django.db.models import Count
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser
from daira.models import Individual, Mol7aka, Report, Job
from sokna.models import SoknaRequest
from cuser.middleware import CuserMiddleware

# My custom AdminSite
class MyAdminSite(admin.AdminSite):

	site_title	= f'{settings.APP_NAME}'
	site_header	= f'{settings.APP_NAME}'
	index_title	= _('Dashboard')

	def index(self, request, extra_context=None):
		if extra_context is None:
			extra_context = {}
		# get current user
		user = CuserMiddleware.get_user()
		
		if not user.is_superuser:
			# Adding my context here
			extra_context.update({'insight': 
				{
					'individual': {
						'male': Individual.objects.filter(mol7aka=user.mol7aka, gender=Individual.MALE).count(),
						'female': Individual.objects.filter(mol7aka=user.mol7aka, gender=Individual.FEMALE).count(),
						'handicapped': Individual.objects.filter(mol7aka=user.mol7aka, handicapped=True).count()
					},
					# 'mol7aka': {
					# 	'employees': CustomUser.objects.filter(mol7aka=user.mol7aka, is_staff=True, is_superuser=False).count(),
					# },
					'reports': {
						'count': Report.objects.filter(mol7aka=user.mol7aka).count()
					},
					'residentials': {
						'approved': SoknaRequest.objects.filter(mol7aka=user.mol7aka, status=SoknaRequest.STATUS.APPROVED).count(),
						'rejected': SoknaRequest.objects.filter(mol7aka=user.mol7aka, status=SoknaRequest.STATUS.REJECTED).count(),
						'pending': SoknaRequest.objects.filter(mol7aka=user.mol7aka, status=SoknaRequest.STATUS.PENDING).count(),
					}
				}
			})		
		else:
			# Adding my context here
			extra_context.update({'insight': 
				{
					'individual': {
						'male': Individual.objects.filter(gender=Individual.MALE).count(),
						'female': Individual.objects.filter(gender=Individual.FEMALE).count(),
						'handicapped': Individual.objects.filter(handicapped=True).count()
					},
					'mol7aka': {
						'count': Mol7aka.objects.count(),
						'employees': CustomUser.objects.filter(is_staff=True, is_superuser=False).count(),
					},
					'reports': {
						'count': Report.objects.count(),
						# get Top 5 reports
						'mol7akat': Mol7aka.objects.values('name').annotate(total_reports=Count('reports')).order_by('-total_reports')[:5]
					},
					# get Top 10 jobs
					'jobs': Job.objects.values('job_name').annotate(dcount=Count('individuals')).order_by('-dcount')[:10],
					'residentials': {
						'approved': SoknaRequest.objects.filter(status=SoknaRequest.STATUS.APPROVED).count(),
						'rejected': SoknaRequest.objects.filter(status=SoknaRequest.STATUS.REJECTED).count(),
						'pending': SoknaRequest.objects.filter(status=SoknaRequest.STATUS.PENDING).count(),
					}
				}
			})
		return super().index(request, extra_context=extra_context)