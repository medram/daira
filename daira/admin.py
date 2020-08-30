from django.contrib import admin
from django.utils.html import mark_safe
from .models import (Address, City, Individual, Street, Report, RelationshipType, Relationship, 
	Job, Amala, Mol7aka)
from .mixins import EmployeeRestrictionMixin

from account.models import CustomUser


class AddressInline(admin.TabularInline):
	model = Address
	extra = 1
	max_num = 4
	autocomplete_fields = ('mol7aka', 'street')
	# exclude = ('mol7aka',)
	# classes = ('collapse',)
	def get_exclude(self, request, obj=None):
		exclude = super().get_exclude(request, obj)
		exclude = [] if exclude is None else list(exclude)

		if not request.user.is_superuser:
			# try to hide "mol7aka"
			try:
				exclude.append('mol7aka')
			except Exception:
				pass
		return exclude


class ReportInline(admin.TabularInline):
	model = Report
	extra = 0
	autocomplete_fields = ('mol7aka',)
	# exclude = ('mol7aka',)
	# classes = ('collapse',)

	def get_exclude(self, request, obj=None):
		exclude = super().get_exclude(request, obj)
		exclude = [] if exclude is None else list(exclude)

		if not request.user.is_superuser:
			# try to hide "mol7aka"
			try:
				exclude.append('mol7aka')
			except Exception:
				pass
		return exclude


@admin.register(Individual)
class IndividualAdmin(EmployeeRestrictionMixin, admin.ModelAdmin):
	list_display = ('CIN', 'firstname', 'lastname', 'get_report_count', 'get_social_status', 'get_income_level', 'handicapped', 'mol7aka', 'created')
	list_filter = ('created', 'mol7aka', 'handicapped', 'income_level', 'social_status')
	search_fields = ('CIN', 'firstname', 'lastname')
	filter_horizontal = ('jobs',)
	inlines = (AddressInline, ReportInline)
	ordering = ('-created',)
	autocomplete_fields = ('mol7aka',)
	date_hierarchy = 'created'

	fieldsets = (
		(None, {
				'fields': ('CIN', ('firstname', 'ar_firstname'), ('lastname', 'ar_lastname'), ('born_d', 'born_m', 'born_y'), 'born_no_d_m', 'gender', 'social_status', 'handicapped', 'income_level', 'jobs', 'mol7aka') 
			}),
		('Card Identite National (CIN)', {
				'fields': ('photo_1', 'photo_2')
			})
	)

	def get_report_count(self, obj):
		return obj.reports.count()
	get_report_count.short_description = 'Reports'


	def get_income_level(self, obj=None):
		if obj.income_level in (obj.IncomeLevel.HIGH, obj.IncomeLevel.VERY_HIGH):
			return mark_safe(f'<span class="badge badge-pill badge-success">{obj.get_income_level_display().upper()}</span>')
		elif obj.income_level == obj.IncomeLevel.MEDIUM:
			return mark_safe(f'<span class="badge badge-pill badge-info">{obj.get_income_level_display().upper()}</span>')
		elif obj.income_level in (obj.IncomeLevel.LOW, obj.IncomeLevel.VERY_LOW):
			return mark_safe(f'<span class="badge badge-pill badge-danger">{obj.get_income_level_display().upper()}</span>')
		else:
			return '-'
	get_income_level.short_description = 'income_level'

	def get_social_status(self, obj=None):
		if obj.social_status == obj.SocialStatus.UNKNOWN:
			return '-'
		else:
			return mark_safe(f'<span class="badge badge-pill badge-secondary">{obj.get_social_status_display().upper()}</span>')
	get_social_status.short_description = 'social_status'
	
	# def get_search_results(self, request, queryset, search_term):
	# 	queryset, use_distinct = super().get_search_results(request, queryset, search_term)
	# 	print('-> ', search_term)
	# 	if not request.user.is_superuser:
	# 		return queryset.filter(mol7aka=request.user.mol7aka), use_distinct
	# 	return queryset, use_distinct


	# def save_model(self, request, obj, form, change):
	# 	if not change:
	# 		obj.mol7aka = request.user.mol7aka
	# 	return super().save_model(request, obj, form, change)



@admin.register(Address)
class AddressAdmin(EmployeeRestrictionMixin, admin.ModelAdmin):
	list_display = ('__str__', 'street', 'city', 'zip_code', 'mol7aka')
	list_filter = ('mol7aka',)
	search_fields = ('address', 'street', 'city', 'zip_code')
	exclude = ('individual',)
	autocomplete_fields = ('street',)
	autocomplete_fields = ('mol7aka', 'street')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	search_fields = ('city',)
	ordering = ('city',)


@admin.register(Street)
class StreetAdmin(EmployeeRestrictionMixin, admin.ModelAdmin):
	list_display = ('street_name', 'individuals_count', 'mol7aka')
	list_filter = ('mol7aka',)
	search_fields = ('street_name',)
	ordering = ('street_name',)
	autocomplete_fields = ('mol7aka',)

	def individuals_count(self, obj):
		return obj.addresses.count()
	individuals_count.short_description = 'Addresses'



@admin.register(Report)
class ReportAdmin(EmployeeRestrictionMixin, admin.ModelAdmin):
	list_display = ('__str__', 'mol7aka', 'updated', 'created')
	list_filter = ('created', 'updated', 'mol7aka')
	search_fields = ('pk', 'individual__CIN', 'individual__firstname', 'individual__lastname')
	autocomplete_fields = ('individual', 'mol7aka')


@admin.register(RelationshipType)
class RelationshipTypesAdmin(admin.ModelAdmin):
	search_fields = ('relationship_name',)
	ordering = ('relationship_name',)


@admin.register(Relationship)
class RelationshipAdmin(EmployeeRestrictionMixin, admin.ModelAdmin):
	list_display = ('id', 'individual_1', 'individual_2', 'mol7aka', 'updated', 'created')
	list_filter = ('created', 'updated', 'mol7aka', 'relationship_type')
	search_fields = ('id', 'individual_1', 'individual_2', 'relationship_type')
	autocomplete_fields = ('individual_1', 'individual_2', 'relationship_type', 'mol7aka')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
	list_display = ('job_name', 'individual_count')
	search_fields = ('job_name',)

	def individual_count(self, obj=None):
		return obj.individuals.count()
	individual_count.short_description = 'Individuals'


@admin.register(Amala)
class AmalaAdmin(admin.ModelAdmin):
	list_display = ('name', 'mol7akat_count')
	search_fields = ('name',)
	ordering = ('name',)

	def mol7akat_count(self, obj=None):
		return obj.mol7akat.count()
	mol7akat_count.short_description = 'Mol7akat'


@admin.register(Mol7aka)
class Mol7akaAdmin(admin.ModelAdmin):
	list_display 	= ('__str__', 'total_employees', 'total_individuals', 'total_handicapped', 'total_reports')
	list_filter 	= ('amala__name',)
	search_fields 	= ('name', 'amala__name')
	ordering 		= ('name', 'name_in_arabic')

	def total_employees(self, obj=None):
		result = CustomUser.objects.filter(mol7aka=obj).count()
		return mark_safe(f"{result} <i class='fas fa-user-tie'></i>")

	def total_individuals(self, obj=None):
		result = Individual.objects.filter(mol7aka=obj).count()
		return mark_safe(f"{result} <i class='fas fa-users text-secondary'></i>")

	def total_handicapped(self, obj=None):
		result = Individual.objects.filter(mol7aka=obj, handicapped=True).count()
		return mark_safe(f"{result} <i class='fas fa-fw fa-wheelchair text-primary'></i>")

	def total_reports(self, obj=None):
		result = Report.objects.filter(mol7aka=obj).count()
		return mark_safe(f"{result} <i class='fas fa-fw fa-copy text-info'></i>")
	