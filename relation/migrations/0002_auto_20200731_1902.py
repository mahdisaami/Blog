# Generated by Django 2.2 on 2020-07-31 14:32

from django.conf import settings
from django.db import migrations, models
import relation.models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='from_user',
            field=models.ForeignKey(on_delete=models.SET(relation.models.create_user), related_name='followings', to=settings.AUTH_USER_MODEL, verbose_name='from user'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='to_user',
            field=models.ForeignKey(on_delete=models.SET(relation.models.create_user), related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='to user'),
        ),
    ]
