from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.common_modesl import BaseModel

User = get_user_model()


class Profile(BaseModel):
    avatar = models.ImageField(upload_to='author/avatars/', blank=True)
    phone_number = models.CharField(_('phone number'), blank=True, max_length=11)
    bio = models.TextField(_('bio'), blank=True)
    user = models.OneToOneField(User, verbose_name=_('profile'), related_name='author', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        db_table = 'profile'

    def __str__(self):
        return "ID: {}\t Username: {}".format(self.id, self.user.username)

