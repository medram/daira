from django.contrib import admin
from django.utils.html import mark_safe
from .models import SoknaRequest

@admin.register(SoknaRequest)
class SoknaRequestAdmin(admin.ModelAdmin):
	list_display = ('id', 'CIN', 'fullname', 'get_gender', 'get_status', 'updated', 'created')
	list_filter = ('created', 'gender', 'status')
	search_fields = ('id', 'CIN', 'firstname', 'lastname')
	date_hierarchy = 'created'
	list_per_page = 5
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

	def get_gender(self, obj=None):
		if obj.gender == obj.GENDER.MALE:
			return mark_safe(f'<i class="fas fa-fw fa-male text-primary"style="font-size: 1.2rem;"></i> {obj.get_gender_display()}')
		elif obj.gender == obj.GENDER.FEMALE:
			return mark_safe(f'<i class="fas fa-fw fa-female text-danger"style="font-size: 1.2rem;"></i> {obj.get_gender_display()}')
		else:
			return '-'
	get_gender.short_description = 'gender'
	get_gender.admin_order_field = 'gender'

	def get_status(self, obj=None):
		if obj.status == obj.STATUS.PENDING:
			return mark_safe(f'<span class="badge badge-pill badge-secondary">{obj.get_status_display().upper()}</span>')
		elif obj.status == obj.STATUS.APPROVED:
			return mark_safe(f'<span class="badge badge-pill badge-success">{obj.get_status_display().upper()}</span>')
		elif obj.status == obj.STATUS.REJECTED:
			return mark_safe(f'<span class="badge badge-pill badge-danger">{obj.get_status_display().upper()}</span>')
		else:
			return '-'
	get_status.short_description = 'status'
	get_status.admin_order_field = 'status'

