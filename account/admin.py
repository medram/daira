from django.contrib import admin
from django.utils.html import format_html, mark_safe
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, CustomGroup

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# unregister the User first.
# admin.site.unregister(User)

# re-register a user admin. 
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     readonly_fields = ('last_login', 'date_joined')

admin.site.unregister(Group)

@admin.register(CustomGroup)
class CustomGroupAdmin(GroupAdmin):
    pass



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display    = ('profile', 'CIN', 'full_name', 'get_gender', 'is_active', 'is_staff', 'date_joined')
    list_display_links = ('CIN', 'full_name')
    # list_editable = ('is_active',)
    readonly_fields = ('get_profile', 'last_login', 'date_joined', 'updated', 'get_password')
    search_fields   = ('CIN', 'first_name', 'last_name', 'email', 'phone')
    list_filter     = ('is_staff', 'is_superuser', 'is_active', 'groups', 'gender')
    ordering        = ('-date_joined',) 
    autocomplete_fields = ('mol7aka',)

    fieldsets = (
        (None, {
                'fields': ('get_profile', 'profile_image')
            }),
        (_('Personal info'), {
                'fields': ('CIN', 'get_password', 'first_name', 'last_name', 'gender', 'phone', 'email', 'address')
            }),
        (_('Permissions'), {
                'fields': ('mol7aka', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            }),
        (_('Important dates'), {
                'fields': ('last_login', 'date_joined', 'updated')
            })
    )

    def get_password(self, obj=None):
        return mark_safe("<a href='../password' class='btn btn-primary btn-sm text-white'><i class='fas fa-key fa-fw'></i> %s</a>" % _('Change Password'))
    get_password.short_description = 'Password'

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('CIN', 'password1', 'password2'),
        }),
    )

    # def get_fieldsets(self, request, obj=None):
    #     # fieldsets = super().get_fieldsets(request, obj)
    #     return fieldsets

    def profile(self, obj):
        return format_html(
            f"<a href=\"{reverse('admin:account_customuser_change', args=(obj.pk,))}\"><img src='{obj.profile_image.url}' width='50' height='50' style='border-radius: 50%; border: 1px solid #CCC;'></a>"
        )

    def get_profile(self, obj):
        return format_html(
            f"<a href=\"{reverse('admin:account_customuser_change', args=(obj.pk,))}\"><img src='{obj.profile_image.url}' style='border-radius: 50%; border: 1px solid #CCC;'></a>"
        )
    get_profile.short_description = _('Avatar')

    def full_name(self, obj):
        full_name = obj.get_full_name().strip()
        if full_name:
            return full_name
        return '-'

    def get_gender(self, obj=None):
        if obj.gender == obj.GENDER.MALE:
            return mark_safe(f'<i class="fas fa-fw fa-male text-primary"style="font-size: 1.2rem;"></i> {obj.get_gender_display()}')
        elif obj.gender == obj.GENDER.FEMALE:
            return mark_safe(f'<i class="fas fa-fw fa-female text-danger"style="font-size: 1.2rem;"></i> {obj.get_gender_display()}')
        else:
            return '-'
    get_gender.short_description = _('Gender')
    get_gender.admin_order_field = 'gender'


    # def save_model(self, request, obj, form, change):
    #     super(admin.ModelAdmin, self).save_model(request, obj, form, change)