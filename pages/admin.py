from django.contrib import admin
from .models import Menu, MenuItem, Page

from adminsortable2.admin import SortableInlineAdminMixin


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('title', 'slug', 'published', 'created', 'updated')
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('title', 'slug')


class InLineMenuItem(SortableInlineAdminMixin, admin.TabularInline):
    model = MenuItem
    extra = 0
    # max_num = 7


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = (InLineMenuItem,)
    list_display = ('name', 'total_menu_items')
    ordering = ('pk',)
    readonly_fields = ('name',)

    def total_menu_items(self, obj):
        return MenuItem.objects.filter(menu=obj.pk).count()

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
