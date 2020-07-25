from django.apps import AppConfig


class DairaConfig(AppConfig):
    name = 'daira'
    verbose_name = 'Database'

    def ready(self):
    	from . import signals
