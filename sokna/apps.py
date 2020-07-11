from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SoknaConfig(AppConfig):
    name = 'sokna'
    verbose_name = _('Residential statement')
