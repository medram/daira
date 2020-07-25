from django.contrib import admin

from .models import (Address, City, Individual, Street, Report, RelationshipType, Relationship, 
	Job, Amala, Mol7aka)


class AddressInline(admin.TabularInline):
	model = Address
	extra = 1
	max_num = 4
	# exclude = ('mol7aka',)
	# classes = ('collapse',)

class ReportInline(admin.TabularInline):
	model = Report
	extra = 0
	# exclude = ('mol7aka',)
	# classes = ('collapse',)

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
	exclude = ('addresses', 'mol7aka')
	list_display = ('CIN', 'firstname', 'lastname', 'born', 'handicapped', 'get_report_count', 'created')
	list_filter = ('created', 'handicapped')
	search_fields = ('CIN', 'firstname', 'lastname')
	filter_horizontal = ('jobs',)
	inlines = (AddressInline, ReportInline)

	def get_report_count(self, obj):
		return obj.reports.count()
	get_report_count.short_description = 'Reports'

	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)

	# def save_model(self, request, obj, form, change):
	# 	if not change:
	# 		obj.mol7aka = request.user.mol7aka
	# 	return super().save_model(request, obj, form, change)



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'street', 'city', 'zip_code')
	search_fields = ('address', 'street', 'city', 'zip_code')
	exclude = ('individual',)

	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)

	def save_model(self, request, obj, form, change):
		print('-> save_model addresses')
		obj.mol7aka = request.user.mol7aka
		return super().save_model(request, obj, form, change)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	search_fields = ('city',)


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
	list_display = ('street_name', 'individuals_count')
	search_fields = ('street_name',)

	def individuals_count(self, obj):
		return obj.addresses.count()
	individuals_count.short_description = 'Addresses'

	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_filter = ('created',)
	search_fields = ('pk', 'individual__CIN', 'individual__firstname', 'individual__lastname')

	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)

	def save_model(self, request, obj, form, change):
		print('-> save_model report')
		obj.mol7aka = request.user.mol7aka
		return super().save_model(request, obj, form, change)



@admin.register(RelationshipType)
class RelationshipTypesAdmin(admin.ModelAdmin):
	pass


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
	list_display = ('id', 'individual_1', 'individual_2', 'updated', 'created')
	list_filter = ('created', 'relationship_type')
	search_fields = ('id', 'individual_1', 'individual_2', 'relationship_type')

	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)


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

	def mol7akat_count(self, obj=None):
		return obj.mol7akat.count()
	mol7akat_count.short_description = 'Mol7akat'


@admin.register(Mol7aka)
class Mol7akaAdmin(admin.ModelAdmin):
	list_filter = ('amala__name',)
	search_fields = ('name', 'amala__name')
	