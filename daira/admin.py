from django.contrib import admin

from .models import (Address, City, Individual, Street, Report, RelationshipType, Relationship, 
	Job, Amala, Mol7aka)


class AddressInline(admin.TabularInline):
	model = Address
	extra = 1
	max_num = 4
	# classes = ('collapse',)

class ReportInline(admin.TabularInline):
	model = Report
	extra = 0
	# classes = ('collapse',)

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
	exclude = ('addresses',)
	list_display = ('CIN', 'firstname', 'lastname', 'born', 'handicapped', 'get_report_count', 'created')
	list_filter = ('created', 'handicapped')
	search_fields = ('CIN', 'firstname', 'lastname')
	filter_horizontal = ('jobs',)
	inlines = (AddressInline, ReportInline)

	def get_report_count(self, obj):
		return obj.reports.count()
	get_report_count.short_description = 'Reports'

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = ('address', 'city', 'zip_code')
	search_fields = ('address', 'city', 'zip_code')
	exclude = ('individual',)

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


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_filter = ('created',)
	search_fields = ('pk', 'individual__CIN', 'individual__firstname', 'individual__lastname')


@admin.register(RelationshipType)
class RelationshipTypesAdmin(admin.ModelAdmin):
	pass

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
	list_display = ('id', 'individual_1', 'individual_2', 'updated', 'created')
	list_filter = ('created', 'relationship_type')
	search_fields = ('id', 'individual_1', 'individual_2', 'relationship_type')


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
	