from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from lib.common_modesl import BaseModel


User = get_user_model()


def create_user():
    user = User.objects.get_or_create(username='deleted account')[0]
    return user


class Relation(BaseModel):
    from_user = models.ForeignKey(
        User, verbose_name=_('from user'), related_name='followers', on_delete=models.SET(create_user)
    )
    to_user = models.ForeignKey(
        User, verbose_name=_('to user'), related_name='followings', on_delete=models.SET(create_user)
    )

    class Meta:
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'
        db_table = "relation"

    def __str__(self):
        return f"User: ({self.from_user}) followed User: ({self.to_user})"
