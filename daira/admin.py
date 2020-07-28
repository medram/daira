from django.contrib import admin

from .models import (Address, City, Individual, Street, Report, RelationshipType, Relationship, 
	Job, Amala, Mol7aka)


class AddressInline(admin.TabularInline):
	model = Address
	extra = 1
	max_num = 4
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
class IndividualAdmin(admin.ModelAdmin):
	exclude = ('addresses', 'mol7aka')
	list_display = ('CIN', 'firstname', 'lastname', 'born', 'handicapped', 'get_report_count', 'mol7aka', 'created')
	list_filter = ('created', 'handicapped', 'mol7aka')
	search_fields = ('CIN', 'firstname', 'lastname')
	filter_horizontal = ('jobs',)
	inlines = (AddressInline, ReportInline)
	ordering = ('-created',)

	def get_report_count(self, obj):
		return obj.reports.count()
	get_report_count.short_description = 'Reports'

	# hide 'mol7aka' from filter
	def get_list_filter(self, request):
		list_filter = super().get_list_filter(request)
		list_filter = [] if list_filter is None else list(list_filter)
		if not request.user.is_superuser:
			try:
				list_filter.remove('mol7aka')
			except Exception:
				pass
		return list_filter

	# hide 'mol7aka' from list_display
	def get_list_display(self, request):
		list_display = super().get_list_display(request)
		list_display = [] if list_display is None else list(list_display)
		if not request.user.is_superuser:
			try:
				list_display.remove('mol7aka')
			except Exception:
				pass
		return list_display


	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)

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
class AddressAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'street', 'city', 'zip_code', 'mol7aka')
	list_filter = ('mol7aka',)
	search_fields = ('address', 'street', 'city', 'zip_code')
	exclude = ('individual',)

	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)


	#Hide 'mol7aka' from showing up.
	def get_fields(self, request, obj=None):
		fields = super().get_fields(request, obj)
		if not request.user.is_superuser:
			#Hide 'mol7aka' from showing up.
			try:
				fields.remove('mol7aka')
			except Exception:
				pass
		return fields

	# hide 'mol7aka' from filter
	def get_list_filter(self, request):
		list_filter = super().get_list_filter(request)
		list_filter = [] if list_filter is None else list(list_filter)
		if not request.user.is_superuser:
			try:
				list_filter.remove('mol7aka')
			except Exception:
				pass
		return list_filter

	# hide 'mol7aka' from list_display
	def get_list_display(self, request):
		list_display = super().get_list_display(request)
		list_display = [] if list_display is None else list(list_display)
		if not request.user.is_superuser:
			try:
				list_display.remove('mol7aka')
			except Exception:
				pass
		return list_display


	# def save_model(self, request, obj, form, change):
	# 	print('-> save_model addresses')
	# 	obj.mol7aka = request.user.mol7aka
	# 	return super().save_model(request, obj, form, change)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	search_fields = ('city',)


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
	list_display = ('street_name', 'individuals_count', 'mol7aka')
	list_filter = ('mol7aka',)
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


	#Hide 'mol7aka' from showing up.
	def get_fields(self, request, obj=None):
		fields = super().get_fields(request, obj)
		if not request.user.is_superuser:
			#Hide 'mol7aka' from showing up.
			try:
				fields.remove('mol7aka')
			except Exception:
				pass
		return fields


	# hide 'mol7aka' from filter
	def get_list_filter(self, request):
		list_filter = super().get_list_filter(request)
		list_filter = [] if list_filter is None else list(list_filter)
		if not request.user.is_superuser:
			try:
				list_filter.remove('mol7aka')
			except Exception:
				pass
		return list_filter

	# hide 'mol7aka' from list_display
	def get_list_display(self, request):
		list_display = super().get_list_display(request)
		list_display = [] if list_display is None else list(list_display)
		if not request.user.is_superuser:
			try:
				list_display.remove('mol7aka')
			except Exception:
				pass
		return list_display


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'mol7aka', 'updated', 'created')
	list_filter = ('created', 'updated', 'mol7aka')
	search_fields = ('pk', 'individual__CIN', 'individual__firstname', 'individual__lastname')

	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)

	#Hide 'mol7aka' from showing up.
	def get_fields(self, request, obj=None):
		fields = super().get_fields(request, obj)
		if not request.user.is_superuser:
			#Hide 'mol7aka' from showing up.
			try:
				fields.remove('mol7aka')
			except Exception:
				pass
		return fields

	# hide 'mol7aka' from filter
	def get_list_filter(self, request):
		list_filter = super().get_list_filter(request)
		list_filter = [] if list_filter is None else list(list_filter)
		if not request.user.is_superuser:
			try:
				list_filter.remove('mol7aka')
			except Exception:
				pass
		return list_filter

	# hide 'mol7aka' from list_display
	def get_list_display(self, request):
		list_display = super().get_list_display(request)
		list_display = [] if list_display is None else list(list_display)
		if not request.user.is_superuser:
			try:
				list_display.remove('mol7aka')
			except Exception:
				pass
		return list_display





@admin.register(RelationshipType)
class RelationshipTypesAdmin(admin.ModelAdmin):
	search_fields = ('relationship_name',)
	ordering = ('-relationship_name',)


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
	list_display = ('id', 'individual_1', 'individual_2', 'mol7aka', 'updated', 'created')
	list_filter = ('created', 'updated', 'mol7aka', 'relationship_type')
	search_fields = ('id', 'individual_1', 'individual_2', 'relationship_type')
	autocomplete_fields = ('individual_1', 'individual_2', 'relationship_type')

	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)

	#Hide 'mol7aka' from showing up.
	def get_fields(self, request, obj=None):
		fields = super().get_fields(request, obj)
		if not request.user.is_superuser:
			#Hide 'mol7aka' from showing up.
			try:
				fields.remove('mol7aka')
			except Exception:
				pass
		return fields

	# hide 'mol7aka' from filter
	def get_list_filter(self, request):
		list_filter = super().get_list_filter(request)
		list_filter = [] if list_filter is None else list(list_filter)
		if not request.user.is_superuser:
			try:
				list_filter.remove('mol7aka')
			except Exception:
				pass
		return list_filter

	# hide 'mol7aka' from list_display
	def get_list_display(self, request):
		list_display = super().get_list_display(request)
		list_display = [] if list_display is None else list(list_display)
		if not request.user.is_superuser:
			try:
				list_display.remove('mol7aka')
			except Exception:
				pass
		return list_display


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
	