from django.contrib import admin

from .models import (Address, City, Individual, Street, Report, RelationshipType, Relationship, 
	Job, Amala, Mol7aka)
from .mixins import EmployeeRestrictionMixin


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
	list_display = ('CIN', 'firstname', 'lastname', 'born', 'handicapped', 'get_report_count', 'mol7aka', 'created')
	list_filter = ('created', 'handicapped', 'mol7aka')
	search_fields = ('CIN', 'firstname', 'lastname')
	filter_horizontal = ('jobs',)
	inlines = (AddressInline, ReportInline)
	ordering = ('-created',)
	autocomplete_fields = ('mol7aka',)

	def get_report_count(self, obj):
		return obj.reports.count()
	get_report_count.short_description = 'Reports'


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
	list_filter = ('amala__name',)
	search_fields = ('name', 'amala__name')
	ordering = ('name', 'name_in_arabic')
	