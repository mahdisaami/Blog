# Generated by Django 2.2 on 2020-08-01 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20200731_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='hashtags',
        ),
    ]
