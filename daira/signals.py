from django.db.models.signals import post_save
from django.dispatch import receiver

from cuser.middleware import CuserMiddleware
from .models import Address, Report, Individual


@receiver(post_save, sender=Individual)
def individual_update(sender, instance, created, **kwargs):
	if created:
		instance.mol7aka = CuserMiddleware.get_user().mol7aka
		instance.save()


@receiver(post_save, sender=Address)
def address_update(sender, instance, created, **kwargs):
	if created:
		instance.mol7aka = CuserMiddleware.get_user().mol7aka
		instance.save()


@receiver(post_save, sender=Report)
def report_update(sender, instance, created, **kwargs):
	if created:
		instance.mol7aka = CuserMiddleware.get_user().mol7aka
		instance.save()