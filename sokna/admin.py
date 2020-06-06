from django.contrib import admin

from .models import SoknaRequest

@admin.register(SoknaRequest)
class SoknaRequestAdmin(admin.ModelAdmin):
	list_display = ('id', 'CIN', 'fullname', 'gender', 'status', 'updated', 'created')
	list_filter = ('created', 'gender', 'status')
	search_fields = ('id', 'CIN', 'firstname', 'lastname')
	date_hierarchy = 'created'
	fieldsets = (
		(None, {
				'fields': ('CIN', ('firstname', 'lastname'), ('born_d', 'born_m', 'born_y'), 'born_no_d_m', 'gender', 'phone', 'address', 'mol7aka')
			}),
		('Card Identite National (CIN)', {
				'fields': ('photo_1', 'photo_2')
			}),
		('Options', {
				'fields': ('status', 'notes')
			})
	)

	def fullname(self, obj=None):
		return f'{obj.firstname} {obj.lastname}'
	fullname.admin_order_field = 'firstname'