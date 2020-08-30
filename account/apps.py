from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name = 'Accounts Managements'

    def ready(self):
    	import account.signals