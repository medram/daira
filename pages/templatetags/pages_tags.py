from django import template

from ..models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('pages/tags/_menu_items.html', takes_context=True)
def main_menu(context):
	return {
		'items': MenuItem.objects.filter(menu=2).order_by('order'),
		'request': context.request
	}


@register.inclusion_tag('pages/tags/_render_menu_item.html', takes_context=True)
def render_menu_item(context, item):
	return {
		'item': item,
		'request': context.request
	}