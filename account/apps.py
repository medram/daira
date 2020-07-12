from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name = 'Accounts Manager (AUTHENTICATION AND AUTHORIZATION)'

    def ready(self):
    	import account.signals