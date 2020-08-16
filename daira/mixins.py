
# A mixin to restrict users/employees.
class EmployeeRestrictionMixin():
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


	# hide 'mol7aka' from fieldsets
	def get_fieldsets(self, request, obj=None):
		fieldsets = super().get_fieldsets(request, obj)
		
		if not request.user.is_superuser:
			new_fieldsets = []
			for title, items in fieldsets:
				items = items.copy()
				try:
					fields = list(items['fields'])
					fields.remove('mol7aka')
					items.update({'fields': fields})
				except Exception:
					pass
				# updating
				new_fieldsets.append((title, items))
			return new_fieldsets
		return fieldsets


	# customize the queryset to list item depends on mol7akat.
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(mol7aka=request.user.mol7aka)

