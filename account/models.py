import os
import secrets
from PIL import Image

from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone

from daira.models import Mol7aka


def _user_profile_path(instance, filename):
    return f"profiles/{secrets.token_hex(16)}.png"

class CustomUserManager(BaseUserManager):
    pass


class CustomUser(AbstractUser):
    CIN     = models.CharField(max_length=16, unique=True)
    USERNAME_FIELD = 'CIN'
    # REQUIRED_FIELDS = (,)

    username = models.CharField(max_length=150, null=True, blank=True, default=timezone.now)

    class GENDER(models.IntegerChoices):
        MALE = (1, _('Male'))
        FEMALE = (2, _('Female'))

    profile_image = models.ImageField(
        upload_to=_user_profile_path, default="profiles/default.jpg", blank=True
    )
    gender  = models.IntegerField(choices=GENDER.choices, default=GENDER.MALE)
    phone   = models.CharField(max_length=10, blank=True, null=True)

    mol7aka = models.ForeignKey(Mol7aka, on_delete=models.CASCADE, related_name='users', null=True, blank=True, verbose_name=_('Administrative attache'))
    
    # status = models.IntegerField(choices=Status.choices, default=Status.APPROVED)
    address = models.CharField(max_length=256, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    # objects = CustomUserManager()


    def save(self, *args, **kwargs):
        # set the token if not exists.
        # if not self.token:
        #     token = secrets.token_hex(32)
        #     try:
        #         while Profile.objects.get(token=token):
        #             token = secrets.token_hex(32)
        #     except Profile.DoesNotExist:
        #         pass
        #     self.token = token

        # getting the old profile images.
        old_user = None
        try:
            old_user = type(self).objects.get(CIN=self.CIN)
        except type(self).DoesNotExist:
            pass

        # save profile
        super().save(*args, **kwargs)

        # resize profile image.
        size = (200, 200)
        try:
            if (
                self.profile_image.name
                and self.profile_image.name != old_user.profile_image.name
            ):
                try:
                    image = Image.open(self.profile_image.path)
                    # image.thumbnail(size)
                    image = image.resize(size)
                    image.save(self.profile_image.path, "PNG")
                except IOError:
                    pass
                else:
                    # removing old profile image.
                    try:
                        os.remove(old_user.profile_image.path)
                    except IOError:
                        pass
        except:
            pass

    def __str__(self):
        return self.get_full_name()



class CustomGroup(Group):
    class Meta:
        verbose_name = 'Group'